from dateutil import parser


class AvailabilityServiceToNotificationTranslator:

    @staticmethod
    def translate(data: dict) -> dict:
        notification = dict()

        notification["whom"] = data["whom"]
        start = parser.parse(data["start"])
        end = parser.parse(data["end"])

        notification["when"] = ["From {} to {}".format(start.strftime("%m/%d/%Y"),
                                                       end.strftime("%m/%d/%Y"))]

        service = data["service"]["name"]
        slo = data["service"]["slo"]
        availability = data["service"]["availability"]
        budget = float(data["service"]["budget"])
        why = []
        if budget < 0:
            template = " SLO: {} has been broken, Current Availability: {} "
            notification["emotion"] = 2
            notification["action"] = "alert"
            notification["what"] = [template.format(slo, availability)]

            features = data["features"]

            for item in features:
                feature_budget = item["budget"]
                feature_availability = item["availability"]
                feature_name = item["name"]
                feature_slo = item["feature_slo"]

                if feature_budget < 0:
                    why.append("Feature: {}, SLO: {} , Availability: {} \n".format(feature_name,
                                                                                   feature_slo,
                                                                                   feature_availability))
        else:
            notification["action"] = "award"
            notification["emotion"] = 4
            notification["what"] = ["SLO: {} is ok, good job, Current Availability: {}".format(slo,
                                                                                               availability)]
        notification["where"] = ["service: {}".format(service)]
        notification["why"] = why
        notification["references"] = data["references"]

        return notification
