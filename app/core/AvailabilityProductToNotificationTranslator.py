from dateutil import parser


class AvailabilityProductToNotificationTranslator:

    @staticmethod
    def translate(data: dict) -> dict:
        notification = dict()

        notification["whom"] = data["whom"]
        start = parser.parse(data["start"])
        end = parser.parse(data["end"])

        notification["when"] = [" {} to {}".format(start.strftime("%m/%d/%Y"),
                                                       end.strftime("%m/%d/%Y"))]

        organization = data["organization"]
        product = data["name"]
        proportion = data["proportion"]
        requests = data["requests"]
        service_min = data["min"]
        service_max = data["max"]
        service_mean = data["mean"]
        feature_coverage = data["feature_coverage"]

        why = []
        if proportion < 1:
            notification["emotion"] = 2
            notification["action"] = "alert"

            template = " {} of services have broken theirs SLO, availability min: {}, average: {}, max: {} "
            notification["what"] = [template.format(proportion, service_min,
                                                    service_mean, service_max)]

            services = data["services"]

            for item in services:
                service_budget = item["budget"]
                service_availability = item["availability"]
                service_name = item["name"]
                service_slo = item["slo"]

                if service_budget < 0:
                    why.append("*Service*: {}, *SLO*: {}, *Availability*: {}, *Budget*: {} \n".format(
                        service_name,
                        service_slo,
                        service_availability,
                        service_budget
                    ))
        else:
            notification["action"] = "award"
            notification["emotion"] = 4
            notification["what"] = [" A good mean SLO {}  performance".format(
                service_mean)]

        notification["where"] = ["*Customer*: {}, *Product*: {}".format(organization, product)]
        notification["why"] = why
        notification["references"] = data["references"]

        return notification
