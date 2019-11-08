from dateutil import parser


class AvailabilitySquadToNotificationTranslator:

    @staticmethod
    def translate(data: dict) -> dict:
        notification = dict()

        notification["whom"] = data["whom"]
        start = parser.parse(data["start"])
        end = parser.parse(data["end"])

        notification["when"] = [" {} to {}".format(start.strftime("%m/%d/%Y"),
                                                   end.strftime("%m/%d/%Y"))]

        organization = data["organization"]
        squad = data["squad"]
        points = float(data["points"])
        why = []
        if points < 0:
            template = "*Squad*: {} has an availability debt"
            notification["emotion"] = 2
            notification["action"] = "alert"
            notification["what"] = [template.format(squad)]

            features = data["features"]

            for item in features:
                feature_product = item["product"]
                feature_service = item["service"]
                feature_feature = item["feature"]
                feature_slo = float(item["slo"])
                feature_availability = float(item["availability"])
                feature_points = float(item["points"])
                if feature_points < 0:
                    why.append("*Product*: {}, *Service*: {}, *Feature*: {}, *SLO*: {}, *Availability*: {} \n".format(
                                                                                   feature_product,
                                                                                   feature_service, feature_feature,
                                                                                   feature_slo, feature_availability))

        else:
            return None
        notification["where"] = ["*Organization*: {}".format(organization)]
        notification["why"] = why
        notification["references"] = data["references"]

        return notification

