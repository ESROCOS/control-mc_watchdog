#!/usr/bin/env python
# ASN.1 Data model
asn1Files = []
asn1Modules = []
exportedTypes = {}
exportedVariables = {}
importedModules = {}
types = {}
variables = {}
asn1Files.append("./dataview-uniq.asn")
asn1Modules.append("Base-Types")
exportedTypes["Base-Types"] = ["Dummy2Base-T", "Base-JointState-MODE", "Base-Time-Resolution", "Base-geometry-SplineBase-CoordinateType", "Base-samples-DepthMap-DEPTH-MEASUREMENT-STATE", "Base-samples-DepthMap-PROJECTION-TYPE", "Base-samples-DepthMap-UNIT-AXIS", "Base-samples-LASER-RANGE-ERRORS", "Base-samples-frame-frame-mode-t", "Base-samples-frame-frame-status-t", "Wrappers-geometry-SplineType", "Base-JointTrajectory", "Std-orogen-typekits-mtype-std-vector-base-JointTransform", "Std-orogen-typekits-mtype-std-vector-base-Waypoint", "Std-orogen-typekits-mtype-std-vector-base-Wrench", "Std-vector-Wrappers-Vector4d", "Std-orogen-typekits-mtype-std-vector-base-Trajectory", "Base-Pose", "Base-TransformWithCovariance", "Base-TwistWithCovariance", "Base-Wrench", "Base-Angle", "Base-JointState", "Base-Pose2D", "Base-PoseUpdateThreshold", "Base-Pressure", "Base-Temperature", "Base-Time", "Base-Trajectory", "Base-Waypoint", "Base-JointLimitRange", "Base-TimeStamped-Base-commands-Motion2D", "Base-LinearAngular6DCommand", "Base-commands-Motion2D", "Base-commands-Speed6D", "Base-samples-BodyState", "Base-samples-IMUSensors", "Base-samples-Motion2D", "Base-samples-Pressure", "Base-samples-RigidBodyAcceleration", "Base-samples-Wrench", "Base-samples-frame-frame-size-t", "Base-JointLimits", "Base-JointTransform", "Base-JointsTrajectory", "Base-NamedVector-Base-JointLimitRange", "Base-NamedVector-Base-JointState", "Base-NamedVector-Base-Wrench", "Base-NamedVector-Base-JointTrajectory", "Base-samples-DepthMap", "Base-samples-DistanceImage", "Base-commands-Joints", "Base-samples-LaserScan", "Base-samples-Pointcloud", "Base-samples-RigidBodyState", "Base-samples-Sonar", "Base-samples-SonarBeam", "Base-samples-SonarScan", "Base-samples-Wrenches", "Base-samples-frame-frame-attrib-t", "Base-JointTransformVector", "Base-NamedVector-Base-JointTransform", "Base-samples-frame-Frame", "Base-samples-frame-FramePair", "Wrappers-AngleAxisd", "Wrappers-Vector2d", "Wrappers-Matrix2d", "Wrappers-Vector3d", "Wrappers-Matrix3d", "Wrappers-Vector4d", "Wrappers-Matrix4d", "Wrappers-Vector6d", "Wrappers-Matrix6d", "Wrappers-MatrixXd", "Wrappers-Quaterniond", "Wrappers-VectorXd", "Base-JointTransform-m", "Base-Pose2D-m", "Base-Pose-m", "Base-TransformWithCovariance-m", "Base-TwistWithCovariance-m", "Base-Waypoint-m", "Base-Wrench-m", "Base-commands-LinearAngular6DCommand-m", "Base-samples-BodyState-m", "Base-samples-IMUSensors-m", "Base-samples-RigidBodyAcceleration-m", "Base-samples-RigidBodyState-m", "Base-samples-Wrench-m", "Base-JointTransformVector-m", "Base-NamedVector-base-JointTransform-m", "Base-NamedVector-base-Wrench-m", "Base-samples-Pointcloud-m", "Base-samples-Wrenches-m", "Wrappers-geometry-Spline", "Base-Trajectory-m", "Wrappers-geometry-Spline-vertices", "Wrappers-geometry-Spline-knots", "Base-samples-Wrenches-m-names", "Base-samples-Pointcloud-m-colors", "Base-samples-Pointcloud-m-points", "Base-NamedVector-base-Wrench-m-names", "Base-NamedVector-base-JointTransform-m-names", "Base-JointTransformVector-m-names", "Wrappers-VectorXd-data", "Wrappers-Quaterniond-im", "Wrappers-MatrixXd-data", "Wrappers-Matrix6d-data", "Wrappers-Vector6d-data", "Wrappers-Matrix4d-data", "Wrappers-Vector4d-data", "Wrappers-Matrix3d-data", "Wrappers-Vector3d-data", "Wrappers-Matrix2d-data", "Wrappers-Vector2d-data", "Wrappers-AngleAxisd-axis", "Base-samples-frame-Frame-attributes", "Base-samples-frame-Frame-image", "Base-NamedVector-Base-JointTransform-elements", "Base-NamedVector-Base-JointTransform-names", "Base-JointTransformVector-elements", "Base-JointTransformVector-names", "Base-samples-Wrenches-elements", "Base-samples-Wrenches-names", "Base-samples-SonarScan-time-beams", "Base-samples-SonarScan-data", "Base-samples-SonarBeam-beam", "Base-samples-Sonar-bins", "Base-samples-Sonar-bearings", "Base-samples-Sonar-timestamps", "Base-samples-Pointcloud-colors", "Base-samples-Pointcloud-points", "Base-samples-LaserScan-remission", "Base-samples-LaserScan-ranges", "Base-commands-Joints-names", "Base-samples-DistanceImage-data", "Base-samples-DepthMap-remissions", "Base-samples-DepthMap-distances", "Base-samples-DepthMap-horizontal-interval", "Base-samples-DepthMap-vertical-interval", "Base-samples-DepthMap-timestamps", "Base-NamedVector-Base-JointTrajectory-elements", "Base-NamedVector-Base-JointTrajectory-names", "Base-NamedVector-Base-Wrench-elements", "Base-NamedVector-Base-Wrench-names", "Base-NamedVector-Base-JointState-names", "Base-NamedVector-Base-JointLimitRange-elements", "Base-NamedVector-Base-JointLimitRange-names", "Base-JointsTrajectory-times-val", "Base-JointsTrajectory-elements", "Base-JointsTrajectory-names", "Base-JointLimits-elements", "Base-JointLimits-names", "T-UInt32", "T-Boolean", "T-Int32", "T-Double", "T-Float", "T-Int64", "T-UInt16", "T-String", "DummyBase-T"]
exportedVariables["Base-Types"] = []
importedModules["Base-Types"] = [{"TASTE-BasicTypes":{"ImportedTypes": ["T-UInt32","T-Boolean","T-Int32"], "ImportedVariables": []}}, {"TASTE-ExtendedTypes":{"ImportedTypes": ["T-Double","T-Float","T-Int64","T-UInt16","T-String"], "ImportedVariables": []}}, {"UserDefs-Base-Types":{"ImportedTypes": ["DummyBase-T"], "ImportedVariables": ["numBase-JointTrajectory","numStd-orogen-typekits-mtype-std-vector-base-JointTransform","numStd-orogen-typekits-mtype-std-vector-base-Waypoint","numStd-orogen-typekits-mtype-std-vector-base-Wrench","numStd-vector-Wrappers-Vector4d","numStd-orogen-typekits-mtype-std-vector-base-Trajectory","numBase-JointLimits-names","numBase-JointLimits-elements","numBase-JointsTrajectory-names","numBase-JointsTrajectory-elements","numBase-JointsTrajectory-times-val","numBase-NamedVector-Base-JointLimitRange-names","numBase-NamedVector-Base-JointLimitRange-elements","numBase-NamedVector-Base-JointState-names","numBase-NamedVector-Base-Wrench-names","numBase-NamedVector-Base-Wrench-elements","numBase-NamedVector-Base-JointTrajectory-names","numBase-NamedVector-Base-JointTrajectory-elements","numBase-samples-DepthMap-timestamps","numBase-samples-DepthMap-vertical-interval","numBase-samples-DepthMap-horizontal-interval","numBase-samples-DepthMap-distances","numBase-samples-DepthMap-remissions","numBase-samples-DistanceImage-data","numBase-commands-Joints-names","numBase-samples-LaserScan-ranges","numBase-samples-LaserScan-remission","numBase-samples-Pointcloud-points","numBase-samples-Pointcloud-colors","numBase-samples-Sonar-timestamps","numBase-samples-Sonar-bearings","numBase-samples-Sonar-bins","numBase-samples-SonarBeam-beam","numBase-samples-SonarScan-data","numBase-samples-SonarScan-time-beams","numBase-samples-Wrenches-names","numBase-samples-Wrenches-elements","numBase-JointTransformVector-names","numBase-JointTransformVector-elements","numBase-NamedVector-Base-JointTransform-names","numBase-NamedVector-Base-JointTransform-elements","numBase-samples-frame-Frame-image","numBase-samples-frame-Frame-attributes","numWrappers-MatrixXd-data","numWrappers-VectorXd-data","numBase-JointTransformVector-m-names","numBase-NamedVector-base-JointTransform-m-names","numBase-NamedVector-base-Wrench-m-names","numBase-samples-Pointcloud-m-points","numBase-samples-Pointcloud-m-colors","numBase-samples-Wrenches-m-names","numWrappers-geometry-Spline-knots","numWrappers-geometry-Spline-vertices"]}}]

types["Dummy2Base-T"] = type("Dummy2Base-T", (object,), {
    "Line": 7, "CharPositionInLine": 4, "type": type("Dummy2Base-T_type", (object,), {
        "Line": 7, "CharPositionInLine": 21, "kind": "ReferenceType", "ReferencedTypeName": "DummyBase-T", "Min": "0", "Max": "4294967295", "ReferencedModName": "UserDefs-Base-Types"
    })
})

types["Base-JointState-MODE"] = type("Base-JointState-MODE", (object,), {
    "Line": 11, "CharPositionInLine": 0, "type": type("Base-JointState-MODE_type", (object,), {
        "Line": 11, "CharPositionInLine": 25, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "base-jointstate-mode-acceleration": type("base_jointstate_mode_acceleration", (object,), {
                "IntValue": 0, "Line": 13, "CharPositionInLine": 4, "EnumID": "base_jointstate_mode_acceleration"
            }),
            "base-jointstate-mode-effort": type("base_jointstate_mode_effort", (object,), {
                "IntValue": 1, "Line": 14, "CharPositionInLine": 4, "EnumID": "base_jointstate_mode_effort"
            }),
            "base-jointstate-mode-position": type("base_jointstate_mode_position", (object,), {
                "IntValue": 2, "Line": 15, "CharPositionInLine": 4, "EnumID": "base_jointstate_mode_position"
            }),
            "base-jointstate-mode-raw": type("base_jointstate_mode_raw", (object,), {
                "IntValue": 3, "Line": 16, "CharPositionInLine": 4, "EnumID": "base_jointstate_mode_raw"
            }),
            "base-jointstate-mode-speed": type("base_jointstate_mode_speed", (object,), {
                "IntValue": 4, "Line": 17, "CharPositionInLine": 4, "EnumID": "base_jointstate_mode_speed"
            }),
            "base-jointstate-mode-unset": type("base_jointstate_mode_unset", (object,), {
                "IntValue": 5, "Line": 18, "CharPositionInLine": 4, "EnumID": "base_jointstate_mode_unset"
            })
        }
    })
})

types["Base-Time-Resolution"] = type("Base-Time-Resolution", (object,), {
    "Line": 23, "CharPositionInLine": 0, "type": type("Base-Time-Resolution_type", (object,), {
        "Line": 23, "CharPositionInLine": 25, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "base-time-resolution-microseconds": type("base_time_resolution_microseconds", (object,), {
                "IntValue": 0, "Line": 25, "CharPositionInLine": 4, "EnumID": "base_time_resolution_microseconds"
            }),
            "base-time-resolution-milliseconds": type("base_time_resolution_milliseconds", (object,), {
                "IntValue": 1, "Line": 26, "CharPositionInLine": 4, "EnumID": "base_time_resolution_milliseconds"
            }),
            "base-time-resolution-seconds": type("base_time_resolution_seconds", (object,), {
                "IntValue": 2, "Line": 27, "CharPositionInLine": 4, "EnumID": "base_time_resolution_seconds"
            })
        }
    })
})

types["Base-geometry-SplineBase-CoordinateType"] = type("Base-geometry-SplineBase-CoordinateType", (object,), {
    "Line": 32, "CharPositionInLine": 0, "type": type("Base-geometry-SplineBase-CoordinateType_type", (object,), {
        "Line": 32, "CharPositionInLine": 44, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "base-geometry-splinebase-coordinatetype-derivative-to-next": type("base_geometry_splinebase_coordinatetype_derivative_to_next", (object,), {
                "IntValue": 0, "Line": 34, "CharPositionInLine": 4, "EnumID": "base_geometry_splinebase_coordinatetype_derivative_to_next"
            }),
            "base-geometry-splinebase-coordinatetype-derivative-to-prior": type("base_geometry_splinebase_coordinatetype_derivative_to_prior", (object,), {
                "IntValue": 1, "Line": 35, "CharPositionInLine": 4, "EnumID": "base_geometry_splinebase_coordinatetype_derivative_to_prior"
            }),
            "base-geometry-splinebase-coordinatetype-knuckle-point": type("base_geometry_splinebase_coordinatetype_knuckle_point", (object,), {
                "IntValue": 2, "Line": 36, "CharPositionInLine": 4, "EnumID": "base_geometry_splinebase_coordinatetype_knuckle_point"
            }),
            "base-geometry-splinebase-coordinatetype-ordinary-point": type("base_geometry_splinebase_coordinatetype_ordinary_point", (object,), {
                "IntValue": 3, "Line": 37, "CharPositionInLine": 4, "EnumID": "base_geometry_splinebase_coordinatetype_ordinary_point"
            }),
            "base-geometry-splinebase-coordinatetype-second-derivative-to-next": type("base_geometry_splinebase_coordinatetype_second_derivative_to_next", (object,), {
                "IntValue": 4, "Line": 38, "CharPositionInLine": 4, "EnumID": "base_geometry_splinebase_coordinatetype_second_derivative_to_next"
            }),
            "base-geometry-splinebase-coordinatetype-second-derivative-to-prior": type("base_geometry_splinebase_coordinatetype_second_derivative_to_prior", (object,), {
                "IntValue": 5, "Line": 39, "CharPositionInLine": 4, "EnumID": "base_geometry_splinebase_coordinatetype_second_derivative_to_prior"
            }),
            "base-geometry-splinebase-coordinatetype-tangent-point-for-next": type("base_geometry_splinebase_coordinatetype_tangent_point_for_next", (object,), {
                "IntValue": 6, "Line": 40, "CharPositionInLine": 4, "EnumID": "base_geometry_splinebase_coordinatetype_tangent_point_for_next"
            }),
            "base-geometry-splinebase-coordinatetype-tangent-point-for-prior": type("base_geometry_splinebase_coordinatetype_tangent_point_for_prior", (object,), {
                "IntValue": 7, "Line": 41, "CharPositionInLine": 4, "EnumID": "base_geometry_splinebase_coordinatetype_tangent_point_for_prior"
            })
        }
    })
})

types["Base-samples-DepthMap-DEPTH-MEASUREMENT-STATE"] = type("Base-samples-DepthMap-DEPTH-MEASUREMENT-STATE", (object,), {
    "Line": 46, "CharPositionInLine": 0, "type": type("Base-samples-DepthMap-DEPTH-MEASUREMENT-STATE_type", (object,), {
        "Line": 46, "CharPositionInLine": 50, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "base-samples-depthmap-depth-measurement-state-measurement-error": type("base_samples_depthmap_depth_measurement_state_measurement_error", (object,), {
                "IntValue": 0, "Line": 48, "CharPositionInLine": 4, "EnumID": "base_samples_depthmap_depth_measurement_state_measurement_error"
            }),
            "base-samples-depthmap-depth-measurement-state-too-far": type("base_samples_depthmap_depth_measurement_state_too_far", (object,), {
                "IntValue": 1, "Line": 49, "CharPositionInLine": 4, "EnumID": "base_samples_depthmap_depth_measurement_state_too_far"
            }),
            "base-samples-depthmap-depth-measurement-state-too-near": type("base_samples_depthmap_depth_measurement_state_too_near", (object,), {
                "IntValue": 2, "Line": 50, "CharPositionInLine": 4, "EnumID": "base_samples_depthmap_depth_measurement_state_too_near"
            }),
            "base-samples-depthmap-depth-measurement-state-valid-measurement": type("base_samples_depthmap_depth_measurement_state_valid_measurement", (object,), {
                "IntValue": 3, "Line": 51, "CharPositionInLine": 4, "EnumID": "base_samples_depthmap_depth_measurement_state_valid_measurement"
            })
        }
    })
})

types["Base-samples-DepthMap-PROJECTION-TYPE"] = type("Base-samples-DepthMap-PROJECTION-TYPE", (object,), {
    "Line": 56, "CharPositionInLine": 0, "type": type("Base-samples-DepthMap-PROJECTION-TYPE_type", (object,), {
        "Line": 56, "CharPositionInLine": 42, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "base-samples-depthmap-projection-type-planar": type("base_samples_depthmap_projection_type_planar", (object,), {
                "IntValue": 0, "Line": 58, "CharPositionInLine": 4, "EnumID": "base_samples_depthmap_projection_type_planar"
            }),
            "base-samples-depthmap-projection-type-polar": type("base_samples_depthmap_projection_type_polar", (object,), {
                "IntValue": 1, "Line": 59, "CharPositionInLine": 4, "EnumID": "base_samples_depthmap_projection_type_polar"
            })
        }
    })
})

types["Base-samples-DepthMap-UNIT-AXIS"] = type("Base-samples-DepthMap-UNIT-AXIS", (object,), {
    "Line": 64, "CharPositionInLine": 0, "type": type("Base-samples-DepthMap-UNIT-AXIS_type", (object,), {
        "Line": 64, "CharPositionInLine": 36, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "base-samples-depthmap-unit-axis-unit-x": type("base_samples_depthmap_unit_axis_unit_x", (object,), {
                "IntValue": 0, "Line": 66, "CharPositionInLine": 4, "EnumID": "base_samples_depthmap_unit_axis_unit_x"
            }),
            "base-samples-depthmap-unit-axis-unit-y": type("base_samples_depthmap_unit_axis_unit_y", (object,), {
                "IntValue": 1, "Line": 67, "CharPositionInLine": 4, "EnumID": "base_samples_depthmap_unit_axis_unit_y"
            }),
            "base-samples-depthmap-unit-axis-unit-z": type("base_samples_depthmap_unit_axis_unit_z", (object,), {
                "IntValue": 2, "Line": 68, "CharPositionInLine": 4, "EnumID": "base_samples_depthmap_unit_axis_unit_z"
            })
        }
    })
})

types["Base-samples-LASER-RANGE-ERRORS"] = type("Base-samples-LASER-RANGE-ERRORS", (object,), {
    "Line": 73, "CharPositionInLine": 0, "type": type("Base-samples-LASER-RANGE-ERRORS_type", (object,), {
        "Line": 73, "CharPositionInLine": 36, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "base-samples-laser-range-errors-end-laser-range-errors": type("base_samples_laser_range_errors_end_laser_range_errors", (object,), {
                "IntValue": 0, "Line": 75, "CharPositionInLine": 4, "EnumID": "base_samples_laser_range_errors_end_laser_range_errors"
            }),
            "base-samples-laser-range-errors-max-range-error": type("base_samples_laser_range_errors_max_range_error", (object,), {
                "IntValue": 1, "Line": 76, "CharPositionInLine": 4, "EnumID": "base_samples_laser_range_errors_max_range_error"
            }),
            "base-samples-laser-range-errors-measurement-error": type("base_samples_laser_range_errors_measurement_error", (object,), {
                "IntValue": 2, "Line": 77, "CharPositionInLine": 4, "EnumID": "base_samples_laser_range_errors_measurement_error"
            }),
            "base-samples-laser-range-errors-other-range-errors": type("base_samples_laser_range_errors_other_range_errors", (object,), {
                "IntValue": 3, "Line": 78, "CharPositionInLine": 4, "EnumID": "base_samples_laser_range_errors_other_range_errors"
            }),
            "base-samples-laser-range-errors-too-far": type("base_samples_laser_range_errors_too_far", (object,), {
                "IntValue": 4, "Line": 79, "CharPositionInLine": 4, "EnumID": "base_samples_laser_range_errors_too_far"
            }),
            "base-samples-laser-range-errors-too-near": type("base_samples_laser_range_errors_too_near", (object,), {
                "IntValue": 5, "Line": 80, "CharPositionInLine": 4, "EnumID": "base_samples_laser_range_errors_too_near"
            })
        }
    })
})

types["Base-samples-frame-frame-mode-t"] = type("Base-samples-frame-frame-mode-t", (object,), {
    "Line": 85, "CharPositionInLine": 0, "type": type("Base-samples-frame-frame-mode-t_type", (object,), {
        "Line": 85, "CharPositionInLine": 36, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "base-samples-frame-frame-mode-t-compressed-modes": type("base_samples_frame_frame_mode_t_compressed_modes", (object,), {
                "IntValue": 0, "Line": 87, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_compressed_modes"
            }),
            "base-samples-frame-frame-mode-t-mode-bayer": type("base_samples_frame_frame_mode_t_mode_bayer", (object,), {
                "IntValue": 1, "Line": 88, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_bayer"
            }),
            "base-samples-frame-frame-mode-t-mode-bayer-bggr": type("base_samples_frame_frame_mode_t_mode_bayer_bggr", (object,), {
                "IntValue": 2, "Line": 89, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_bayer_bggr"
            }),
            "base-samples-frame-frame-mode-t-mode-bayer-gbrg": type("base_samples_frame_frame_mode_t_mode_bayer_gbrg", (object,), {
                "IntValue": 3, "Line": 90, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_bayer_gbrg"
            }),
            "base-samples-frame-frame-mode-t-mode-bayer-grbg": type("base_samples_frame_frame_mode_t_mode_bayer_grbg", (object,), {
                "IntValue": 4, "Line": 91, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_bayer_grbg"
            }),
            "base-samples-frame-frame-mode-t-mode-bayer-rggb": type("base_samples_frame_frame_mode_t_mode_bayer_rggb", (object,), {
                "IntValue": 5, "Line": 92, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_bayer_rggb"
            }),
            "base-samples-frame-frame-mode-t-mode-bgr": type("base_samples_frame_frame_mode_t_mode_bgr", (object,), {
                "IntValue": 6, "Line": 93, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_bgr"
            }),
            "base-samples-frame-frame-mode-t-mode-grayscale": type("base_samples_frame_frame_mode_t_mode_grayscale", (object,), {
                "IntValue": 7, "Line": 94, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_grayscale"
            }),
            "base-samples-frame-frame-mode-t-mode-jpeg": type("base_samples_frame_frame_mode_t_mode_jpeg", (object,), {
                "IntValue": 8, "Line": 95, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_jpeg"
            }),
            "base-samples-frame-frame-mode-t-mode-pjpg": type("base_samples_frame_frame_mode_t_mode_pjpg", (object,), {
                "IntValue": 9, "Line": 96, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_pjpg"
            }),
            "base-samples-frame-frame-mode-t-mode-png": type("base_samples_frame_frame_mode_t_mode_png", (object,), {
                "IntValue": 10, "Line": 97, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_png"
            }),
            "base-samples-frame-frame-mode-t-mode-rgb": type("base_samples_frame_frame_mode_t_mode_rgb", (object,), {
                "IntValue": 11, "Line": 98, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_rgb"
            }),
            "base-samples-frame-frame-mode-t-mode-rgb32": type("base_samples_frame_frame_mode_t_mode_rgb32", (object,), {
                "IntValue": 12, "Line": 99, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_rgb32"
            }),
            "base-samples-frame-frame-mode-t-mode-undefined": type("base_samples_frame_frame_mode_t_mode_undefined", (object,), {
                "IntValue": 13, "Line": 100, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_undefined"
            }),
            "base-samples-frame-frame-mode-t-mode-uyvy": type("base_samples_frame_frame_mode_t_mode_uyvy", (object,), {
                "IntValue": 14, "Line": 101, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_mode_uyvy"
            }),
            "base-samples-frame-frame-mode-t-raw-modes": type("base_samples_frame_frame_mode_t_raw_modes", (object,), {
                "IntValue": 15, "Line": 102, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_mode_t_raw_modes"
            })
        }
    })
})

types["Base-samples-frame-frame-status-t"] = type("Base-samples-frame-frame-status-t", (object,), {
    "Line": 107, "CharPositionInLine": 0, "type": type("Base-samples-frame-frame-status-t_type", (object,), {
        "Line": 107, "CharPositionInLine": 38, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "base-samples-frame-frame-status-t-status-empty": type("base_samples_frame_frame_status_t_status_empty", (object,), {
                "IntValue": 0, "Line": 109, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_status_t_status_empty"
            }),
            "base-samples-frame-frame-status-t-status-invalid": type("base_samples_frame_frame_status_t_status_invalid", (object,), {
                "IntValue": 1, "Line": 110, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_status_t_status_invalid"
            }),
            "base-samples-frame-frame-status-t-status-valid": type("base_samples_frame_frame_status_t_status_valid", (object,), {
                "IntValue": 2, "Line": 111, "CharPositionInLine": 4, "EnumID": "base_samples_frame_frame_status_t_status_valid"
            })
        }
    })
})

types["Wrappers-geometry-SplineType"] = type("Wrappers-geometry-SplineType", (object,), {
    "Line": 116, "CharPositionInLine": 0, "type": type("Wrappers-geometry-SplineType_type", (object,), {
        "Line": 116, "CharPositionInLine": 33, "kind": "EnumeratedType", "Extensible": "False", "ValuesAutoCalculated": "False", "EnumValues": {
            "wrappers-geometry-splinetype-degenerate": type("wrappers_geometry_splinetype_degenerate", (object,), {
                "IntValue": 0, "Line": 118, "CharPositionInLine": 4, "EnumID": "wrappers_geometry_splinetype_degenerate"
            }),
            "wrappers-geometry-splinetype-polynomial-bezier": type("wrappers_geometry_splinetype_polynomial_bezier", (object,), {
                "IntValue": 1, "Line": 119, "CharPositionInLine": 4, "EnumID": "wrappers_geometry_splinetype_polynomial_bezier"
            }),
            "wrappers-geometry-splinetype-polynomial-bspline": type("wrappers_geometry_splinetype_polynomial_bspline", (object,), {
                "IntValue": 2, "Line": 120, "CharPositionInLine": 4, "EnumID": "wrappers_geometry_splinetype_polynomial_bspline"
            }),
            "wrappers-geometry-splinetype-rational-bezier": type("wrappers_geometry_splinetype_rational_bezier", (object,), {
                "IntValue": 3, "Line": 121, "CharPositionInLine": 4, "EnumID": "wrappers_geometry_splinetype_rational_bezier"
            }),
            "wrappers-geometry-splinetype-rational-bspline": type("wrappers_geometry_splinetype_rational_bspline", (object,), {
                "IntValue": 4, "Line": 122, "CharPositionInLine": 4, "EnumID": "wrappers_geometry_splinetype_rational_bspline"
            })
        }
    })
})

types["Base-JointTrajectory"] = type("Base-JointTrajectory", (object,), {
    "Line": 131, "CharPositionInLine": 0, "type": type("Base-JointTrajectory_type", (object,), {
        "Line": 127, "CharPositionInLine": 62, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 127, "CharPositionInLine": 108, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointState"
        })
    })
})

types["Std-orogen-typekits-mtype-std-vector-base-JointTransform"] = type("Std-orogen-typekits-mtype-std-vector-base-JointTransform", (object,), {
    "Line": 139, "CharPositionInLine": 0, "type": type("Std-orogen-typekits-mtype-std-vector-base-JointTransform_type", (object,), {
        "Line": 135, "CharPositionInLine": 134, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 135, "CharPositionInLine": 216, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTransform-m"
        })
    })
})

types["Std-orogen-typekits-mtype-std-vector-base-Waypoint"] = type("Std-orogen-typekits-mtype-std-vector-base-Waypoint", (object,), {
    "Line": 147, "CharPositionInLine": 0, "type": type("Std-orogen-typekits-mtype-std-vector-base-Waypoint_type", (object,), {
        "Line": 143, "CharPositionInLine": 122, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 143, "CharPositionInLine": 198, "kind": "ReferenceType", "ReferencedTypeName": "Base-Waypoint-m"
        })
    })
})

types["Std-orogen-typekits-mtype-std-vector-base-Wrench"] = type("Std-orogen-typekits-mtype-std-vector-base-Wrench", (object,), {
    "Line": 155, "CharPositionInLine": 0, "type": type("Std-orogen-typekits-mtype-std-vector-base-Wrench_type", (object,), {
        "Line": 151, "CharPositionInLine": 118, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 151, "CharPositionInLine": 192, "kind": "ReferenceType", "ReferencedTypeName": "Base-Wrench-m"
        })
    })
})

types["Std-vector-Wrappers-Vector4d"] = type("Std-vector-Wrappers-Vector4d", (object,), {
    "Line": 163, "CharPositionInLine": 0, "type": type("Std-vector-Wrappers-Vector4d_type", (object,), {
        "Line": 159, "CharPositionInLine": 78, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 159, "CharPositionInLine": 132, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector4d"
        })
    })
})

types["Std-orogen-typekits-mtype-std-vector-base-Trajectory"] = type("Std-orogen-typekits-mtype-std-vector-base-Trajectory", (object,), {
    "Line": 171, "CharPositionInLine": 0, "type": type("Std-orogen-typekits-mtype-std-vector-base-Trajectory_type", (object,), {
        "Line": 167, "CharPositionInLine": 126, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 167, "CharPositionInLine": 204, "kind": "ReferenceType", "ReferencedTypeName": "Base-Trajectory-m"
        })
    })
})

types["Base-Pose"] = type("Base-Pose", (object,), {
    "Line": 175, "CharPositionInLine": 0, "type": type("Base-Pose_type", (object,), {
        "Line": 175, "CharPositionInLine": 14, "kind": "SequenceType", "Children": {
            "position": type("position", (object,), {
                "Optional": "False", "Line": 177, "CharPositionInLine": 4, "type": type("position_type", (object,), {
                    "Line": 177, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "orientation": type("orientation", (object,), {
                "Optional": "False", "Line": 178, "CharPositionInLine": 4, "type": type("orientation_type", (object,), {
                    "Line": 178, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Quaterniond"
                })
            })
        }
    })
})

types["Base-TransformWithCovariance"] = type("Base-TransformWithCovariance", (object,), {
    "Line": 183, "CharPositionInLine": 0, "type": type("Base-TransformWithCovariance_type", (object,), {
        "Line": 183, "CharPositionInLine": 33, "kind": "SequenceType", "Children": {
            "translation": type("translation", (object,), {
                "Optional": "False", "Line": 185, "CharPositionInLine": 4, "type": type("translation_type", (object,), {
                    "Line": 185, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "orientation": type("orientation", (object,), {
                "Optional": "False", "Line": 186, "CharPositionInLine": 4, "type": type("orientation_type", (object,), {
                    "Line": 186, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Quaterniond"
                })
            }),
            "cov": type("cov", (object,), {
                "Optional": "False", "Line": 187, "CharPositionInLine": 4, "type": type("cov_type", (object,), {
                    "Line": 187, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix6d"
                })
            })
        }
    })
})

types["Base-TwistWithCovariance"] = type("Base-TwistWithCovariance", (object,), {
    "Line": 192, "CharPositionInLine": 0, "type": type("Base-TwistWithCovariance_type", (object,), {
        "Line": 192, "CharPositionInLine": 29, "kind": "SequenceType", "Children": {
            "vel": type("vel", (object,), {
                "Optional": "False", "Line": 194, "CharPositionInLine": 4, "type": type("vel_type", (object,), {
                    "Line": 194, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "rot": type("rot", (object,), {
                "Optional": "False", "Line": 195, "CharPositionInLine": 4, "type": type("rot_type", (object,), {
                    "Line": 195, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov": type("cov", (object,), {
                "Optional": "False", "Line": 196, "CharPositionInLine": 4, "type": type("cov_type", (object,), {
                    "Line": 196, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix6d"
                })
            })
        }
    })
})

types["Base-Wrench"] = type("Base-Wrench", (object,), {
    "Line": 201, "CharPositionInLine": 0, "type": type("Base-Wrench_type", (object,), {
        "Line": 201, "CharPositionInLine": 16, "kind": "SequenceType", "Children": {
            "force": type("force", (object,), {
                "Optional": "False", "Line": 203, "CharPositionInLine": 4, "type": type("force_type", (object,), {
                    "Line": 203, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "torque": type("torque", (object,), {
                "Optional": "False", "Line": 204, "CharPositionInLine": 4, "type": type("torque_type", (object,), {
                    "Line": 204, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            })
        }
    })
})

types["Base-Angle"] = type("Base-Angle", (object,), {
    "Line": 209, "CharPositionInLine": 0, "type": type("Base-Angle_type", (object,), {
        "Line": 209, "CharPositionInLine": 15, "kind": "SequenceType", "Children": {
            "rad": type("rad", (object,), {
                "Optional": "False", "Line": 211, "CharPositionInLine": 4, "type": type("rad_type", (object,), {
                    "Line": 211, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-JointState"] = type("Base-JointState", (object,), {
    "Line": 216, "CharPositionInLine": 0, "type": type("Base-JointState_type", (object,), {
        "Line": 216, "CharPositionInLine": 20, "kind": "SequenceType", "Children": {
            "position": type("position", (object,), {
                "Optional": "False", "Line": 218, "CharPositionInLine": 4, "type": type("position_type", (object,), {
                    "Line": 218, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "speed": type("speed", (object,), {
                "Optional": "False", "Line": 219, "CharPositionInLine": 4, "type": type("speed_type", (object,), {
                    "Line": 219, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "effort": type("effort", (object,), {
                "Optional": "False", "Line": 220, "CharPositionInLine": 4, "type": type("effort_type", (object,), {
                    "Line": 220, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "raw": type("raw", (object,), {
                "Optional": "False", "Line": 221, "CharPositionInLine": 4, "type": type("raw_type", (object,), {
                    "Line": 221, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "acceleration": type("acceleration", (object,), {
                "Optional": "False", "Line": 222, "CharPositionInLine": 4, "type": type("acceleration_type", (object,), {
                    "Line": 222, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-Pose2D"] = type("Base-Pose2D", (object,), {
    "Line": 227, "CharPositionInLine": 0, "type": type("Base-Pose2D_type", (object,), {
        "Line": 227, "CharPositionInLine": 16, "kind": "SequenceType", "Children": {
            "position": type("position", (object,), {
                "Optional": "False", "Line": 229, "CharPositionInLine": 4, "type": type("position_type", (object,), {
                    "Line": 229, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector2d"
                })
            }),
            "orientation": type("orientation", (object,), {
                "Optional": "False", "Line": 230, "CharPositionInLine": 4, "type": type("orientation_type", (object,), {
                    "Line": 230, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-PoseUpdateThreshold"] = type("Base-PoseUpdateThreshold", (object,), {
    "Line": 235, "CharPositionInLine": 0, "type": type("Base-PoseUpdateThreshold_type", (object,), {
        "Line": 235, "CharPositionInLine": 29, "kind": "SequenceType", "Children": {
            "distance": type("distance", (object,), {
                "Optional": "False", "Line": 237, "CharPositionInLine": 4, "type": type("distance_type", (object,), {
                    "Line": 237, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "angle": type("angle", (object,), {
                "Optional": "False", "Line": 238, "CharPositionInLine": 4, "type": type("angle_type", (object,), {
                    "Line": 238, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-Pressure"] = type("Base-Pressure", (object,), {
    "Line": 243, "CharPositionInLine": 0, "type": type("Base-Pressure_type", (object,), {
        "Line": 243, "CharPositionInLine": 18, "kind": "SequenceType", "Children": {
            "pascal": type("pascal", (object,), {
                "Optional": "False", "Line": 245, "CharPositionInLine": 4, "type": type("pascal_type", (object,), {
                    "Line": 245, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-Temperature"] = type("Base-Temperature", (object,), {
    "Line": 250, "CharPositionInLine": 0, "type": type("Base-Temperature_type", (object,), {
        "Line": 250, "CharPositionInLine": 21, "kind": "SequenceType", "Children": {
            "kelvin": type("kelvin", (object,), {
                "Optional": "False", "Line": 252, "CharPositionInLine": 4, "type": type("kelvin_type", (object,), {
                    "Line": 252, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-Time"] = type("Base-Time", (object,), {
    "Line": 257, "CharPositionInLine": 0, "type": type("Base-Time_type", (object,), {
        "Line": 257, "CharPositionInLine": 14, "kind": "SequenceType", "Children": {
            "microseconds": type("microseconds", (object,), {
                "Optional": "False", "Line": 259, "CharPositionInLine": 4, "type": type("microseconds_type", (object,), {
                    "Line": 259, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "T-Int64", "Min": "-9223372036854775807", "Max": "9223372036854775807", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-Trajectory"] = type("Base-Trajectory", (object,), {
    "Line": 264, "CharPositionInLine": 0, "type": type("Base-Trajectory_type", (object,), {
        "Line": 264, "CharPositionInLine": 20, "kind": "SequenceType", "Children": {
            "speed": type("speed", (object,), {
                "Optional": "False", "Line": 266, "CharPositionInLine": 4, "type": type("speed_type", (object,), {
                    "Line": 266, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "spline": type("spline", (object,), {
                "Optional": "False", "Line": 267, "CharPositionInLine": 4, "type": type("spline_type", (object,), {
                    "Line": 267, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-geometry-Spline"
                })
            })
        }
    })
})

types["Base-Waypoint"] = type("Base-Waypoint", (object,), {
    "Line": 272, "CharPositionInLine": 0, "type": type("Base-Waypoint_type", (object,), {
        "Line": 272, "CharPositionInLine": 18, "kind": "SequenceType", "Children": {
            "position": type("position", (object,), {
                "Optional": "False", "Line": 274, "CharPositionInLine": 4, "type": type("position_type", (object,), {
                    "Line": 274, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "heading": type("heading", (object,), {
                "Optional": "False", "Line": 275, "CharPositionInLine": 4, "type": type("heading_type", (object,), {
                    "Line": 275, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "tol-position": type("tol-position", (object,), {
                "Optional": "False", "Line": 276, "CharPositionInLine": 4, "type": type("tol-position_type", (object,), {
                    "Line": 276, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "tol-heading": type("tol-heading", (object,), {
                "Optional": "False", "Line": 277, "CharPositionInLine": 4, "type": type("tol-heading_type", (object,), {
                    "Line": 277, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-JointLimitRange"] = type("Base-JointLimitRange", (object,), {
    "Line": 282, "CharPositionInLine": 0, "type": type("Base-JointLimitRange_type", (object,), {
        "Line": 282, "CharPositionInLine": 25, "kind": "SequenceType", "Children": {
            "min": type("min", (object,), {
                "Optional": "False", "Line": 284, "CharPositionInLine": 4, "type": type("min_type", (object,), {
                    "Line": 284, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointState"
                })
            }),
            "max": type("max", (object,), {
                "Optional": "False", "Line": 285, "CharPositionInLine": 4, "type": type("max_type", (object,), {
                    "Line": 285, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointState"
                })
            })
        }
    })
})

types["Base-TimeStamped-Base-commands-Motion2D"] = type("Base-TimeStamped-Base-commands-Motion2D", (object,), {
    "Line": 290, "CharPositionInLine": 0, "type": type("Base-TimeStamped-Base-commands-Motion2D_type", (object,), {
        "Line": 290, "CharPositionInLine": 44, "kind": "SequenceType", "Children": {
            "translation": type("translation", (object,), {
                "Optional": "False", "Line": 292, "CharPositionInLine": 4, "type": type("translation_type", (object,), {
                    "Line": 292, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "rotation": type("rotation", (object,), {
                "Optional": "False", "Line": 293, "CharPositionInLine": 4, "type": type("rotation_type", (object,), {
                    "Line": 293, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "heading": type("heading", (object,), {
                "Optional": "False", "Line": 294, "CharPositionInLine": 4, "type": type("heading_type", (object,), {
                    "Line": 294, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            }),
            "time": type("time", (object,), {
                "Optional": "False", "Line": 295, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 295, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            })
        }
    })
})

types["Base-LinearAngular6DCommand"] = type("Base-LinearAngular6DCommand", (object,), {
    "Line": 300, "CharPositionInLine": 0, "type": type("Base-LinearAngular6DCommand_type", (object,), {
        "Line": 300, "CharPositionInLine": 32, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 302, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 302, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "linear": type("linear", (object,), {
                "Optional": "False", "Line": 303, "CharPositionInLine": 4, "type": type("linear_type", (object,), {
                    "Line": 303, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "angular": type("angular", (object,), {
                "Optional": "False", "Line": 304, "CharPositionInLine": 4, "type": type("angular_type", (object,), {
                    "Line": 304, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            })
        }
    })
})

types["Base-commands-Motion2D"] = type("Base-commands-Motion2D", (object,), {
    "Line": 309, "CharPositionInLine": 0, "type": type("Base-commands-Motion2D_type", (object,), {
        "Line": 309, "CharPositionInLine": 27, "kind": "SequenceType", "Children": {
            "translation": type("translation", (object,), {
                "Optional": "False", "Line": 311, "CharPositionInLine": 4, "type": type("translation_type", (object,), {
                    "Line": 311, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "rotation": type("rotation", (object,), {
                "Optional": "False", "Line": 312, "CharPositionInLine": 4, "type": type("rotation_type", (object,), {
                    "Line": 312, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "heading": type("heading", (object,), {
                "Optional": "False", "Line": 313, "CharPositionInLine": 4, "type": type("heading_type", (object,), {
                    "Line": 313, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            })
        }
    })
})

types["Base-commands-Speed6D"] = type("Base-commands-Speed6D", (object,), {
    "Line": 318, "CharPositionInLine": 0, "type": type("Base-commands-Speed6D_type", (object,), {
        "Line": 318, "CharPositionInLine": 26, "kind": "SequenceType", "Children": {
            "surge": type("surge", (object,), {
                "Optional": "False", "Line": 320, "CharPositionInLine": 4, "type": type("surge_type", (object,), {
                    "Line": 320, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "sway": type("sway", (object,), {
                "Optional": "False", "Line": 321, "CharPositionInLine": 4, "type": type("sway_type", (object,), {
                    "Line": 321, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "heave": type("heave", (object,), {
                "Optional": "False", "Line": 322, "CharPositionInLine": 4, "type": type("heave_type", (object,), {
                    "Line": 322, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "roll": type("roll", (object,), {
                "Optional": "False", "Line": 323, "CharPositionInLine": 4, "type": type("roll_type", (object,), {
                    "Line": 323, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "pitch": type("pitch", (object,), {
                "Optional": "False", "Line": 324, "CharPositionInLine": 4, "type": type("pitch_type", (object,), {
                    "Line": 324, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "yaw": type("yaw", (object,), {
                "Optional": "False", "Line": 325, "CharPositionInLine": 4, "type": type("yaw_type", (object,), {
                    "Line": 325, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-samples-BodyState"] = type("Base-samples-BodyState", (object,), {
    "Line": 330, "CharPositionInLine": 0, "type": type("Base-samples-BodyState_type", (object,), {
        "Line": 330, "CharPositionInLine": 27, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 332, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 332, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "pose": type("pose", (object,), {
                "Optional": "False", "Line": 333, "CharPositionInLine": 4, "type": type("pose_type", (object,), {
                    "Line": 333, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-TransformWithCovariance"
                })
            }),
            "velocity": type("velocity", (object,), {
                "Optional": "False", "Line": 334, "CharPositionInLine": 4, "type": type("velocity_type", (object,), {
                    "Line": 334, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Base-TwistWithCovariance"
                })
            })
        }
    })
})

types["Base-samples-IMUSensors"] = type("Base-samples-IMUSensors", (object,), {
    "Line": 339, "CharPositionInLine": 0, "type": type("Base-samples-IMUSensors_type", (object,), {
        "Line": 339, "CharPositionInLine": 28, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 341, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 341, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "acc": type("acc", (object,), {
                "Optional": "False", "Line": 342, "CharPositionInLine": 4, "type": type("acc_type", (object,), {
                    "Line": 342, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "gyro": type("gyro", (object,), {
                "Optional": "False", "Line": 343, "CharPositionInLine": 4, "type": type("gyro_type", (object,), {
                    "Line": 343, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "mag": type("mag", (object,), {
                "Optional": "False", "Line": 344, "CharPositionInLine": 4, "type": type("mag_type", (object,), {
                    "Line": 344, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            })
        }
    })
})

types["Base-samples-Motion2D"] = type("Base-samples-Motion2D", (object,), {
    "Line": 349, "CharPositionInLine": 0, "type": type("Base-samples-Motion2D_type", (object,), {
        "Line": 349, "CharPositionInLine": 26, "kind": "SequenceType", "Children": {
            "translation": type("translation", (object,), {
                "Optional": "False", "Line": 351, "CharPositionInLine": 4, "type": type("translation_type", (object,), {
                    "Line": 351, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "rotation": type("rotation", (object,), {
                "Optional": "False", "Line": 352, "CharPositionInLine": 4, "type": type("rotation_type", (object,), {
                    "Line": 352, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "heading": type("heading", (object,), {
                "Optional": "False", "Line": 353, "CharPositionInLine": 4, "type": type("heading_type", (object,), {
                    "Line": 353, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            }),
            "time": type("time", (object,), {
                "Optional": "False", "Line": 354, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 354, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            })
        }
    })
})

types["Base-samples-Pressure"] = type("Base-samples-Pressure", (object,), {
    "Line": 359, "CharPositionInLine": 0, "type": type("Base-samples-Pressure_type", (object,), {
        "Line": 359, "CharPositionInLine": 26, "kind": "SequenceType", "Children": {
            "pascal": type("pascal", (object,), {
                "Optional": "False", "Line": 361, "CharPositionInLine": 4, "type": type("pascal_type", (object,), {
                    "Line": 361, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "time": type("time", (object,), {
                "Optional": "False", "Line": 362, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 362, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            })
        }
    })
})

types["Base-samples-RigidBodyAcceleration"] = type("Base-samples-RigidBodyAcceleration", (object,), {
    "Line": 367, "CharPositionInLine": 0, "type": type("Base-samples-RigidBodyAcceleration_type", (object,), {
        "Line": 367, "CharPositionInLine": 39, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 369, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 369, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "acceleration": type("acceleration", (object,), {
                "Optional": "False", "Line": 370, "CharPositionInLine": 4, "type": type("acceleration_type", (object,), {
                    "Line": 370, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-acceleration": type("cov-acceleration", (object,), {
                "Optional": "False", "Line": 371, "CharPositionInLine": 4, "type": type("cov-acceleration_type", (object,), {
                    "Line": 371, "CharPositionInLine": 22, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            }),
            "angular-acceleration": type("angular-acceleration", (object,), {
                "Optional": "False", "Line": 372, "CharPositionInLine": 4, "type": type("angular-acceleration_type", (object,), {
                    "Line": 372, "CharPositionInLine": 26, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-angular-acceleration": type("cov-angular-acceleration", (object,), {
                "Optional": "False", "Line": 373, "CharPositionInLine": 4, "type": type("cov-angular-acceleration_type", (object,), {
                    "Line": 373, "CharPositionInLine": 30, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            })
        }
    })
})

types["Base-samples-Wrench"] = type("Base-samples-Wrench", (object,), {
    "Line": 378, "CharPositionInLine": 0, "type": type("Base-samples-Wrench_type", (object,), {
        "Line": 378, "CharPositionInLine": 24, "kind": "SequenceType", "Children": {
            "force": type("force", (object,), {
                "Optional": "False", "Line": 380, "CharPositionInLine": 4, "type": type("force_type", (object,), {
                    "Line": 380, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "torque": type("torque", (object,), {
                "Optional": "False", "Line": 381, "CharPositionInLine": 4, "type": type("torque_type", (object,), {
                    "Line": 381, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "time": type("time", (object,), {
                "Optional": "False", "Line": 382, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 382, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            })
        }
    })
})

types["Base-samples-frame-frame-size-t"] = type("Base-samples-frame-frame-size-t", (object,), {
    "Line": 387, "CharPositionInLine": 0, "type": type("Base-samples-frame-frame-size-t_type", (object,), {
        "Line": 387, "CharPositionInLine": 36, "kind": "SequenceType", "Children": {
            "width": type("width", (object,), {
                "Optional": "False", "Line": 389, "CharPositionInLine": 4, "type": type("width_type", (object,), {
                    "Line": 389, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt16", "Min": "0", "Max": "65535", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "height": type("height", (object,), {
                "Optional": "False", "Line": 390, "CharPositionInLine": 4, "type": type("height_type", (object,), {
                    "Line": 390, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt16", "Min": "0", "Max": "65535", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-JointLimits"] = type("Base-JointLimits", (object,), {
    "Line": 403, "CharPositionInLine": 0, "type": type("Base-JointLimits_type", (object,), {
        "Line": 395, "CharPositionInLine": 99, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 397, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointLimits-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 398, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointLimits-elements", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-JointTransform"] = type("Base-JointTransform", (object,), {
    "Line": 407, "CharPositionInLine": 0, "type": type("Base-JointTransform_type", (object,), {
        "Line": 407, "CharPositionInLine": 24, "kind": "SequenceType", "Children": {
            "sourceframe": type("sourceframe", (object,), {
                "Optional": "False", "Line": 409, "CharPositionInLine": 4, "type": type("sourceframe_type", (object,), {
                    "Line": 409, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "targetframe": type("targetframe", (object,), {
                "Optional": "False", "Line": 410, "CharPositionInLine": 4, "type": type("targetframe_type", (object,), {
                    "Line": 410, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "rotationaxis": type("rotationaxis", (object,), {
                "Optional": "False", "Line": 411, "CharPositionInLine": 4, "type": type("rotationaxis_type", (object,), {
                    "Line": 411, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            })
        }
    })
})

types["Base-JointsTrajectory"] = type("Base-JointsTrajectory", (object,), {
    "Line": 425, "CharPositionInLine": 0, "type": type("Base-JointsTrajectory_type", (object,), {
        "Line": 416, "CharPositionInLine": 160, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 418, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointsTrajectory-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 419, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointsTrajectory-elements", "Min": "1", "Max": "200"
                })
            }),
            "times-val": type("times-val", (object,), {
                "Optional": "False", "Line": 420, "CharPositionInLine": 4, "type": type("times-val_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointsTrajectory-times-val", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-NamedVector-Base-JointLimitRange"] = type("Base-NamedVector-Base-JointLimitRange", (object,), {
    "Line": 437, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointLimitRange_type", (object,), {
        "Line": 429, "CharPositionInLine": 162, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 431, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-Base-JointLimitRange-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 432, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-Base-JointLimitRange-elements", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-NamedVector-Base-JointState"] = type("Base-NamedVector-Base-JointState", (object,), {
    "Line": 449, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointState_type", (object,), {
        "Line": 441, "CharPositionInLine": 91, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 443, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-Base-JointState-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 444, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 444, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTrajectory", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-NamedVector-Base-Wrench"] = type("Base-NamedVector-Base-Wrench", (object,), {
    "Line": 461, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-Wrench_type", (object,), {
        "Line": 453, "CharPositionInLine": 135, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 455, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-Base-Wrench-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 456, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-Base-Wrench-elements", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-NamedVector-Base-JointTrajectory"] = type("Base-NamedVector-Base-JointTrajectory", (object,), {
    "Line": 473, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointTrajectory_type", (object,), {
        "Line": 465, "CharPositionInLine": 162, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 467, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-Base-JointTrajectory-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 468, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-Base-JointTrajectory-elements", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-samples-DepthMap"] = type("Base-samples-DepthMap", (object,), {
    "Line": 493, "CharPositionInLine": 0, "type": type("Base-samples-DepthMap_type", (object,), {
        "Line": 477, "CharPositionInLine": 277, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 479, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 479, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "timestamps": type("timestamps", (object,), {
                "Optional": "False", "Line": 480, "CharPositionInLine": 4, "type": type("timestamps_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-DepthMap-timestamps", "Min": "1", "Max": "200"
                })
            }),
            "vertical-projection": type("vertical-projection", (object,), {
                "Optional": "False", "Line": 481, "CharPositionInLine": 4, "type": type("vertical-projection_type", (object,), {
                    "Line": 481, "CharPositionInLine": 25, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-DepthMap-PROJECTION-TYPE"
                })
            }),
            "horizontal-projection": type("horizontal-projection", (object,), {
                "Optional": "False", "Line": 482, "CharPositionInLine": 4, "type": type("horizontal-projection_type", (object,), {
                    "Line": 482, "CharPositionInLine": 27, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-DepthMap-PROJECTION-TYPE"
                })
            }),
            "vertical-interval": type("vertical-interval", (object,), {
                "Optional": "False", "Line": 483, "CharPositionInLine": 4, "type": type("vertical-interval_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-DepthMap-vertical-interval", "Min": "1", "Max": "200"
                })
            }),
            "horizontal-interval": type("horizontal-interval", (object,), {
                "Optional": "False", "Line": 484, "CharPositionInLine": 4, "type": type("horizontal-interval_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-DepthMap-horizontal-interval", "Min": "1", "Max": "200"
                })
            }),
            "vertical-size": type("vertical-size", (object,), {
                "Optional": "False", "Line": 485, "CharPositionInLine": 4, "type": type("vertical-size_type", (object,), {
                    "Line": 485, "CharPositionInLine": 19, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "horizontal-size": type("horizontal-size", (object,), {
                "Optional": "False", "Line": 486, "CharPositionInLine": 4, "type": type("horizontal-size_type", (object,), {
                    "Line": 486, "CharPositionInLine": 21, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "distances": type("distances", (object,), {
                "Optional": "False", "Line": 487, "CharPositionInLine": 4, "type": type("distances_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-DepthMap-distances", "Min": "1", "Max": "200"
                })
            }),
            "remissions": type("remissions", (object,), {
                "Optional": "False", "Line": 488, "CharPositionInLine": 4, "type": type("remissions_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-DepthMap-remissions", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-samples-DistanceImage"] = type("Base-samples-DistanceImage", (object,), {
    "Line": 511, "CharPositionInLine": 0, "type": type("Base-samples-DistanceImage_type", (object,), {
        "Line": 497, "CharPositionInLine": 78, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 499, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 499, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "width": type("width", (object,), {
                "Optional": "False", "Line": 500, "CharPositionInLine": 4, "type": type("width_type", (object,), {
                    "Line": 500, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt16", "Min": "0", "Max": "65535", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "height": type("height", (object,), {
                "Optional": "False", "Line": 501, "CharPositionInLine": 4, "type": type("height_type", (object,), {
                    "Line": 501, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt16", "Min": "0", "Max": "65535", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "scale-x": type("scale-x", (object,), {
                "Optional": "False", "Line": 502, "CharPositionInLine": 4, "type": type("scale-x_type", (object,), {
                    "Line": 502, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "scale-y": type("scale-y", (object,), {
                "Optional": "False", "Line": 503, "CharPositionInLine": 4, "type": type("scale-y_type", (object,), {
                    "Line": 503, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "center-x": type("center-x", (object,), {
                "Optional": "False", "Line": 504, "CharPositionInLine": 4, "type": type("center-x_type", (object,), {
                    "Line": 504, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "center-y": type("center-y", (object,), {
                "Optional": "False", "Line": 505, "CharPositionInLine": 4, "type": type("center-y_type", (object,), {
                    "Line": 505, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "data": type("data", (object,), {
                "Optional": "False", "Line": 506, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-DistanceImage-data", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-commands-Joints"] = type("Base-commands-Joints", (object,), {
    "Line": 524, "CharPositionInLine": 0, "type": type("Base-commands-Joints_type", (object,), {
        "Line": 515, "CharPositionInLine": 67, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 517, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-commands-Joints-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 518, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 518, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTrajectory", "Min": "1", "Max": "200"
                })
            }),
            "time": type("time", (object,), {
                "Optional": "False", "Line": 519, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 519, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            })
        }
    })
})

types["Base-samples-LaserScan"] = type("Base-samples-LaserScan", (object,), {
    "Line": 542, "CharPositionInLine": 0, "type": type("Base-samples-LaserScan_type", (object,), {
        "Line": 528, "CharPositionInLine": 119, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 530, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 530, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "start-angle": type("start-angle", (object,), {
                "Optional": "False", "Line": 531, "CharPositionInLine": 4, "type": type("start-angle_type", (object,), {
                    "Line": 531, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "angular-resolution": type("angular-resolution", (object,), {
                "Optional": "False", "Line": 532, "CharPositionInLine": 4, "type": type("angular-resolution_type", (object,), {
                    "Line": 532, "CharPositionInLine": 24, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "speed": type("speed", (object,), {
                "Optional": "False", "Line": 533, "CharPositionInLine": 4, "type": type("speed_type", (object,), {
                    "Line": 533, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "ranges": type("ranges", (object,), {
                "Optional": "False", "Line": 534, "CharPositionInLine": 4, "type": type("ranges_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-LaserScan-ranges", "Min": "1", "Max": "200"
                })
            }),
            "minrange": type("minrange", (object,), {
                "Optional": "False", "Line": 535, "CharPositionInLine": 4, "type": type("minrange_type", (object,), {
                    "Line": 535, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "maxrange": type("maxrange", (object,), {
                "Optional": "False", "Line": 536, "CharPositionInLine": 4, "type": type("maxrange_type", (object,), {
                    "Line": 536, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "remission": type("remission", (object,), {
                "Optional": "False", "Line": 537, "CharPositionInLine": 4, "type": type("remission_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-LaserScan-remission", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-samples-Pointcloud"] = type("Base-samples-Pointcloud", (object,), {
    "Line": 555, "CharPositionInLine": 0, "type": type("Base-samples-Pointcloud_type", (object,), {
        "Line": 546, "CharPositionInLine": 119, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 548, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 548, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "points": type("points", (object,), {
                "Optional": "False", "Line": 549, "CharPositionInLine": 4, "type": type("points_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Pointcloud-points", "Min": "1", "Max": "200"
                })
            }),
            "colors": type("colors", (object,), {
                "Optional": "False", "Line": 550, "CharPositionInLine": 4, "type": type("colors_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Pointcloud-colors", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-samples-RigidBodyState"] = type("Base-samples-RigidBodyState", (object,), {
    "Line": 559, "CharPositionInLine": 0, "type": type("Base-samples-RigidBodyState_type", (object,), {
        "Line": 559, "CharPositionInLine": 32, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 561, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 561, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "sourceframe": type("sourceframe", (object,), {
                "Optional": "False", "Line": 562, "CharPositionInLine": 4, "type": type("sourceframe_type", (object,), {
                    "Line": 562, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "targetframe": type("targetframe", (object,), {
                "Optional": "False", "Line": 563, "CharPositionInLine": 4, "type": type("targetframe_type", (object,), {
                    "Line": 563, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "position": type("position", (object,), {
                "Optional": "False", "Line": 564, "CharPositionInLine": 4, "type": type("position_type", (object,), {
                    "Line": 564, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-position": type("cov-position", (object,), {
                "Optional": "False", "Line": 565, "CharPositionInLine": 4, "type": type("cov-position_type", (object,), {
                    "Line": 565, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            }),
            "orientation": type("orientation", (object,), {
                "Optional": "False", "Line": 566, "CharPositionInLine": 4, "type": type("orientation_type", (object,), {
                    "Line": 566, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Quaterniond"
                })
            }),
            "cov-orientation": type("cov-orientation", (object,), {
                "Optional": "False", "Line": 567, "CharPositionInLine": 4, "type": type("cov-orientation_type", (object,), {
                    "Line": 567, "CharPositionInLine": 21, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            }),
            "velocity": type("velocity", (object,), {
                "Optional": "False", "Line": 568, "CharPositionInLine": 4, "type": type("velocity_type", (object,), {
                    "Line": 568, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-velocity": type("cov-velocity", (object,), {
                "Optional": "False", "Line": 569, "CharPositionInLine": 4, "type": type("cov-velocity_type", (object,), {
                    "Line": 569, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            }),
            "angular-velocity": type("angular-velocity", (object,), {
                "Optional": "False", "Line": 570, "CharPositionInLine": 4, "type": type("angular-velocity_type", (object,), {
                    "Line": 570, "CharPositionInLine": 22, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-angular-velocity": type("cov-angular-velocity", (object,), {
                "Optional": "False", "Line": 571, "CharPositionInLine": 4, "type": type("cov-angular-velocity_type", (object,), {
                    "Line": 571, "CharPositionInLine": 26, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            })
        }
    })
})

types["Base-samples-Sonar"] = type("Base-samples-Sonar", (object,), {
    "Line": 592, "CharPositionInLine": 0, "type": type("Base-samples-Sonar_type", (object,), {
        "Line": 576, "CharPositionInLine": 148, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 578, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 578, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "timestamps": type("timestamps", (object,), {
                "Optional": "False", "Line": 579, "CharPositionInLine": 4, "type": type("timestamps_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Sonar-timestamps", "Min": "1", "Max": "200"
                })
            }),
            "bin-duration": type("bin-duration", (object,), {
                "Optional": "False", "Line": 580, "CharPositionInLine": 4, "type": type("bin-duration_type", (object,), {
                    "Line": 580, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "beam-width": type("beam-width", (object,), {
                "Optional": "False", "Line": 581, "CharPositionInLine": 4, "type": type("beam-width_type", (object,), {
                    "Line": 581, "CharPositionInLine": 16, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            }),
            "beam-height": type("beam-height", (object,), {
                "Optional": "False", "Line": 582, "CharPositionInLine": 4, "type": type("beam-height_type", (object,), {
                    "Line": 582, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            }),
            "bearings": type("bearings", (object,), {
                "Optional": "False", "Line": 583, "CharPositionInLine": 4, "type": type("bearings_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Sonar-bearings", "Min": "1", "Max": "200"
                })
            }),
            "speed-of-sound": type("speed-of-sound", (object,), {
                "Optional": "False", "Line": 584, "CharPositionInLine": 4, "type": type("speed-of-sound_type", (object,), {
                    "Line": 584, "CharPositionInLine": 20, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "bin-count": type("bin-count", (object,), {
                "Optional": "False", "Line": 585, "CharPositionInLine": 4, "type": type("bin-count_type", (object,), {
                    "Line": 585, "CharPositionInLine": 15, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "beam-count": type("beam-count", (object,), {
                "Optional": "False", "Line": 586, "CharPositionInLine": 4, "type": type("beam-count_type", (object,), {
                    "Line": 586, "CharPositionInLine": 16, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "bins": type("bins", (object,), {
                "Optional": "False", "Line": 587, "CharPositionInLine": 4, "type": type("bins_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Sonar-bins", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-samples-SonarBeam"] = type("Base-samples-SonarBeam", (object,), {
    "Line": 609, "CharPositionInLine": 0, "type": type("Base-samples-SonarBeam_type", (object,), {
        "Line": 596, "CharPositionInLine": 70, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 598, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 598, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "bearing": type("bearing", (object,), {
                "Optional": "False", "Line": 599, "CharPositionInLine": 4, "type": type("bearing_type", (object,), {
                    "Line": 599, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            }),
            "sampling-interval": type("sampling-interval", (object,), {
                "Optional": "False", "Line": 600, "CharPositionInLine": 4, "type": type("sampling-interval_type", (object,), {
                    "Line": 600, "CharPositionInLine": 23, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "speed-of-sound": type("speed-of-sound", (object,), {
                "Optional": "False", "Line": 601, "CharPositionInLine": 4, "type": type("speed-of-sound_type", (object,), {
                    "Line": 601, "CharPositionInLine": 20, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "beamwidth-horizontal": type("beamwidth-horizontal", (object,), {
                "Optional": "False", "Line": 602, "CharPositionInLine": 4, "type": type("beamwidth-horizontal_type", (object,), {
                    "Line": 602, "CharPositionInLine": 26, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "beamwidth-vertical": type("beamwidth-vertical", (object,), {
                "Optional": "False", "Line": 603, "CharPositionInLine": 4, "type": type("beamwidth-vertical_type", (object,), {
                    "Line": 603, "CharPositionInLine": 24, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "beam": type("beam", (object,), {
                "Optional": "False", "Line": 604, "CharPositionInLine": 4, "type": type("beam_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-SonarBeam-beam", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-samples-SonarScan"] = type("Base-samples-SonarScan", (object,), {
    "Line": 632, "CharPositionInLine": 0, "type": type("Base-samples-SonarScan_type", (object,), {
        "Line": 613, "CharPositionInLine": 118, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 615, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 615, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "data": type("data", (object,), {
                "Optional": "False", "Line": 616, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-SonarScan-data", "Min": "1", "Max": "200"
                })
            }),
            "time-beams": type("time-beams", (object,), {
                "Optional": "False", "Line": 617, "CharPositionInLine": 4, "type": type("time-beams_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-SonarScan-time-beams", "Min": "1", "Max": "200"
                })
            }),
            "number-of-beams": type("number-of-beams", (object,), {
                "Optional": "False", "Line": 618, "CharPositionInLine": 4, "type": type("number-of-beams_type", (object,), {
                    "Line": 618, "CharPositionInLine": 21, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt16", "Min": "0", "Max": "65535", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "number-of-bins": type("number-of-bins", (object,), {
                "Optional": "False", "Line": 619, "CharPositionInLine": 4, "type": type("number-of-bins_type", (object,), {
                    "Line": 619, "CharPositionInLine": 20, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt16", "Min": "0", "Max": "65535", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "start-bearing": type("start-bearing", (object,), {
                "Optional": "False", "Line": 620, "CharPositionInLine": 4, "type": type("start-bearing_type", (object,), {
                    "Line": 620, "CharPositionInLine": 19, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            }),
            "angular-resolution": type("angular-resolution", (object,), {
                "Optional": "False", "Line": 621, "CharPositionInLine": 4, "type": type("angular-resolution_type", (object,), {
                    "Line": 621, "CharPositionInLine": 24, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            }),
            "sampling-interval": type("sampling-interval", (object,), {
                "Optional": "False", "Line": 622, "CharPositionInLine": 4, "type": type("sampling-interval_type", (object,), {
                    "Line": 622, "CharPositionInLine": 23, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "speed-of-sound": type("speed-of-sound", (object,), {
                "Optional": "False", "Line": 623, "CharPositionInLine": 4, "type": type("speed-of-sound_type", (object,), {
                    "Line": 623, "CharPositionInLine": 20, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "beamwidth-horizontal": type("beamwidth-horizontal", (object,), {
                "Optional": "False", "Line": 624, "CharPositionInLine": 4, "type": type("beamwidth-horizontal_type", (object,), {
                    "Line": 624, "CharPositionInLine": 26, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            }),
            "beamwidth-vertical": type("beamwidth-vertical", (object,), {
                "Optional": "False", "Line": 625, "CharPositionInLine": 4, "type": type("beamwidth-vertical_type", (object,), {
                    "Line": 625, "CharPositionInLine": 24, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
                })
            }),
            "memory-layout-column": type("memory-layout-column", (object,), {
                "Optional": "False", "Line": 626, "CharPositionInLine": 4, "type": type("memory-layout-column_type", (object,), {
                    "Line": 626, "CharPositionInLine": 26, "kind": "ReferenceType", "ReferencedTypeName": "T-Boolean", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "polar-coordinates": type("polar-coordinates", (object,), {
                "Optional": "False", "Line": 627, "CharPositionInLine": 4, "type": type("polar-coordinates_type", (object,), {
                    "Line": 627, "CharPositionInLine": 23, "kind": "ReferenceType", "ReferencedTypeName": "T-Boolean", "ReferencedModName": "TASTE-BasicTypes"
                })
            })
        }
    })
})

types["Base-samples-Wrenches"] = type("Base-samples-Wrenches", (object,), {
    "Line": 645, "CharPositionInLine": 0, "type": type("Base-samples-Wrenches_type", (object,), {
        "Line": 636, "CharPositionInLine": 114, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 638, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Wrenches-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 639, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Wrenches-elements", "Min": "1", "Max": "200"
                })
            }),
            "time": type("time", (object,), {
                "Optional": "False", "Line": 640, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 640, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            })
        }
    })
})

types["Base-samples-frame-frame-attrib-t"] = type("Base-samples-frame-frame-attrib-t", (object,), {
    "Line": 649, "CharPositionInLine": 0, "type": type("Base-samples-frame-frame-attrib-t_type", (object,), {
        "Line": 649, "CharPositionInLine": 38, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 651, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 651, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "name-val": type("name-val", (object,), {
                "Optional": "False", "Line": 652, "CharPositionInLine": 4, "type": type("name-val_type", (object,), {
                    "Line": 652, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-JointTransformVector"] = type("Base-JointTransformVector", (object,), {
    "Line": 665, "CharPositionInLine": 0, "type": type("Base-JointTransformVector_type", (object,), {
        "Line": 657, "CharPositionInLine": 126, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 659, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTransformVector-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 660, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTransformVector-elements", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-NamedVector-Base-JointTransform"] = type("Base-NamedVector-Base-JointTransform", (object,), {
    "Line": 677, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointTransform_type", (object,), {
        "Line": 669, "CharPositionInLine": 159, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 671, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-Base-JointTransform-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 672, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-Base-JointTransform-elements", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-samples-frame-Frame"] = type("Base-samples-frame-Frame", (object,), {
    "Line": 697, "CharPositionInLine": 0, "type": type("Base-samples-frame-Frame_type", (object,), {
        "Line": 681, "CharPositionInLine": 125, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 683, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 683, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "received-time": type("received-time", (object,), {
                "Optional": "False", "Line": 684, "CharPositionInLine": 4, "type": type("received-time_type", (object,), {
                    "Line": 684, "CharPositionInLine": 19, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "image": type("image", (object,), {
                "Optional": "False", "Line": 685, "CharPositionInLine": 4, "type": type("image_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-frame-Frame-image", "Min": "1", "Max": "200"
                })
            }),
            "attributes": type("attributes", (object,), {
                "Optional": "False", "Line": 686, "CharPositionInLine": 4, "type": type("attributes_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-frame-Frame-attributes", "Min": "1", "Max": "200"
                })
            }),
            "size-val": type("size-val", (object,), {
                "Optional": "False", "Line": 687, "CharPositionInLine": 4, "type": type("size-val_type", (object,), {
                    "Line": 687, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-frame-frame-size-t"
                })
            }),
            "data-depth": type("data-depth", (object,), {
                "Optional": "False", "Line": 688, "CharPositionInLine": 4, "type": type("data-depth_type", (object,), {
                    "Line": 688, "CharPositionInLine": 16, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "pixel-size": type("pixel-size", (object,), {
                "Optional": "False", "Line": 689, "CharPositionInLine": 4, "type": type("pixel-size_type", (object,), {
                    "Line": 689, "CharPositionInLine": 16, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "row-size": type("row-size", (object,), {
                "Optional": "False", "Line": 690, "CharPositionInLine": 4, "type": type("row-size_type", (object,), {
                    "Line": 690, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "frame-mode": type("frame-mode", (object,), {
                "Optional": "False", "Line": 691, "CharPositionInLine": 4, "type": type("frame-mode_type", (object,), {
                    "Line": 691, "CharPositionInLine": 16, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-frame-frame-mode-t"
                })
            }),
            "frame-status": type("frame-status", (object,), {
                "Optional": "False", "Line": 692, "CharPositionInLine": 4, "type": type("frame-status_type", (object,), {
                    "Line": 692, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-frame-frame-status-t"
                })
            })
        }
    })
})

types["Base-samples-frame-FramePair"] = type("Base-samples-frame-FramePair", (object,), {
    "Line": 701, "CharPositionInLine": 0, "type": type("Base-samples-frame-FramePair_type", (object,), {
        "Line": 701, "CharPositionInLine": 33, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 703, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 703, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "first": type("first", (object,), {
                "Optional": "False", "Line": 704, "CharPositionInLine": 4, "type": type("first_type", (object,), {
                    "Line": 704, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-frame-Frame"
                })
            }),
            "second": type("second", (object,), {
                "Optional": "False", "Line": 705, "CharPositionInLine": 4, "type": type("second_type", (object,), {
                    "Line": 705, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-frame-Frame"
                })
            }),
            "id": type("id", (object,), {
                "Optional": "False", "Line": 706, "CharPositionInLine": 4, "type": type("id_type", (object,), {
                    "Line": 706, "CharPositionInLine": 8, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            })
        }
    })
})

types["Wrappers-AngleAxisd"] = type("Wrappers-AngleAxisd", (object,), {
    "Line": 711, "CharPositionInLine": 0, "type": type("Wrappers-AngleAxisd_type", (object,), {
        "Line": 711, "CharPositionInLine": 24, "kind": "SequenceType", "Children": {
            "angle": type("angle", (object,), {
                "Optional": "False", "Line": 713, "CharPositionInLine": 4, "type": type("angle_type", (object,), {
                    "Line": 713, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "axis": type("axis", (object,), {
                "Optional": "False", "Line": 714, "CharPositionInLine": 4, "type": type("axis_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-AngleAxisd-axis", "Min": "1", "Max": "3"
                })
            })
        }
    })
})

types["Wrappers-Vector2d"] = type("Wrappers-Vector2d", (object,), {
    "Line": 719, "CharPositionInLine": 0, "type": type("Wrappers-Vector2d_type", (object,), {
        "Line": 719, "CharPositionInLine": 22, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 721, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector2d-data", "Min": "1", "Max": "2"
                })
            })
        }
    })
})

types["Wrappers-Matrix2d"] = type("Wrappers-Matrix2d", (object,), {
    "Line": 726, "CharPositionInLine": 0, "type": type("Wrappers-Matrix2d_type", (object,), {
        "Line": 726, "CharPositionInLine": 22, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 728, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix2d-data", "Min": "1", "Max": "4"
                })
            })
        }
    })
})

types["Wrappers-Vector3d"] = type("Wrappers-Vector3d", (object,), {
    "Line": 733, "CharPositionInLine": 0, "type": type("Wrappers-Vector3d_type", (object,), {
        "Line": 733, "CharPositionInLine": 22, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 735, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d-data", "Min": "1", "Max": "3"
                })
            })
        }
    })
})

types["Wrappers-Matrix3d"] = type("Wrappers-Matrix3d", (object,), {
    "Line": 740, "CharPositionInLine": 0, "type": type("Wrappers-Matrix3d_type", (object,), {
        "Line": 740, "CharPositionInLine": 22, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 742, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d-data", "Min": "1", "Max": "9"
                })
            })
        }
    })
})

types["Wrappers-Vector4d"] = type("Wrappers-Vector4d", (object,), {
    "Line": 747, "CharPositionInLine": 0, "type": type("Wrappers-Vector4d_type", (object,), {
        "Line": 747, "CharPositionInLine": 22, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 749, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector4d-data", "Min": "1", "Max": "4"
                })
            })
        }
    })
})

types["Wrappers-Matrix4d"] = type("Wrappers-Matrix4d", (object,), {
    "Line": 754, "CharPositionInLine": 0, "type": type("Wrappers-Matrix4d_type", (object,), {
        "Line": 754, "CharPositionInLine": 22, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 756, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix4d-data", "Min": "1", "Max": "16"
                })
            })
        }
    })
})

types["Wrappers-Vector6d"] = type("Wrappers-Vector6d", (object,), {
    "Line": 761, "CharPositionInLine": 0, "type": type("Wrappers-Vector6d_type", (object,), {
        "Line": 761, "CharPositionInLine": 22, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 763, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector6d-data", "Min": "1", "Max": "6"
                })
            })
        }
    })
})

types["Wrappers-Matrix6d"] = type("Wrappers-Matrix6d", (object,), {
    "Line": 768, "CharPositionInLine": 0, "type": type("Wrappers-Matrix6d_type", (object,), {
        "Line": 768, "CharPositionInLine": 22, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 770, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix6d-data", "Min": "1", "Max": "36"
                })
            })
        }
    })
})

types["Wrappers-MatrixXd"] = type("Wrappers-MatrixXd", (object,), {
    "Line": 784, "CharPositionInLine": 0, "type": type("Wrappers-MatrixXd_type", (object,), {
        "Line": 775, "CharPositionInLine": 60, "kind": "SequenceType", "Children": {
            "rows": type("rows", (object,), {
                "Optional": "False", "Line": 777, "CharPositionInLine": 4, "type": type("rows_type", (object,), {
                    "Line": 777, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "T-Int32", "Min": "-2147483648", "Max": "2147483647", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "cols": type("cols", (object,), {
                "Optional": "False", "Line": 778, "CharPositionInLine": 4, "type": type("cols_type", (object,), {
                    "Line": 778, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "T-Int32", "Min": "-2147483648", "Max": "2147483647", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "data": type("data", (object,), {
                "Optional": "False", "Line": 779, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-MatrixXd-data", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Wrappers-Quaterniond"] = type("Wrappers-Quaterniond", (object,), {
    "Line": 788, "CharPositionInLine": 0, "type": type("Wrappers-Quaterniond_type", (object,), {
        "Line": 788, "CharPositionInLine": 25, "kind": "SequenceType", "Children": {
            "im": type("im", (object,), {
                "Optional": "False", "Line": 790, "CharPositionInLine": 4, "type": type("im_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Quaterniond-im", "Min": "1", "Max": "3"
                })
            }),
            "re": type("re", (object,), {
                "Optional": "False", "Line": 791, "CharPositionInLine": 4, "type": type("re_type", (object,), {
                    "Line": 791, "CharPositionInLine": 8, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Wrappers-VectorXd"] = type("Wrappers-VectorXd", (object,), {
    "Line": 803, "CharPositionInLine": 0, "type": type("Wrappers-VectorXd_type", (object,), {
        "Line": 796, "CharPositionInLine": 60, "kind": "SequenceType", "Children": {
            "data": type("data", (object,), {
                "Optional": "False", "Line": 798, "CharPositionInLine": 4, "type": type("data_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-VectorXd-data", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-JointTransform-m"] = type("Base-JointTransform-m", (object,), {
    "Line": 807, "CharPositionInLine": 0, "type": type("Base-JointTransform-m_type", (object,), {
        "Line": 807, "CharPositionInLine": 26, "kind": "SequenceType", "Children": {
            "sourceframe": type("sourceframe", (object,), {
                "Optional": "False", "Line": 809, "CharPositionInLine": 4, "type": type("sourceframe_type", (object,), {
                    "Line": 809, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "targetframe": type("targetframe", (object,), {
                "Optional": "False", "Line": 810, "CharPositionInLine": 4, "type": type("targetframe_type", (object,), {
                    "Line": 810, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "rotationaxis": type("rotationaxis", (object,), {
                "Optional": "False", "Line": 811, "CharPositionInLine": 4, "type": type("rotationaxis_type", (object,), {
                    "Line": 811, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            })
        }
    })
})

types["Base-Pose2D-m"] = type("Base-Pose2D-m", (object,), {
    "Line": 816, "CharPositionInLine": 0, "type": type("Base-Pose2D-m_type", (object,), {
        "Line": 816, "CharPositionInLine": 18, "kind": "SequenceType", "Children": {
            "position": type("position", (object,), {
                "Optional": "False", "Line": 818, "CharPositionInLine": 4, "type": type("position_type", (object,), {
                    "Line": 818, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector2d"
                })
            }),
            "orientation": type("orientation", (object,), {
                "Optional": "False", "Line": 819, "CharPositionInLine": 4, "type": type("orientation_type", (object,), {
                    "Line": 819, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-Pose-m"] = type("Base-Pose-m", (object,), {
    "Line": 824, "CharPositionInLine": 0, "type": type("Base-Pose-m_type", (object,), {
        "Line": 824, "CharPositionInLine": 16, "kind": "SequenceType", "Children": {
            "position": type("position", (object,), {
                "Optional": "False", "Line": 826, "CharPositionInLine": 4, "type": type("position_type", (object,), {
                    "Line": 826, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "orientation": type("orientation", (object,), {
                "Optional": "False", "Line": 827, "CharPositionInLine": 4, "type": type("orientation_type", (object,), {
                    "Line": 827, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Quaterniond"
                })
            })
        }
    })
})

types["Base-TransformWithCovariance-m"] = type("Base-TransformWithCovariance-m", (object,), {
    "Line": 832, "CharPositionInLine": 0, "type": type("Base-TransformWithCovariance-m_type", (object,), {
        "Line": 832, "CharPositionInLine": 35, "kind": "SequenceType", "Children": {
            "translation": type("translation", (object,), {
                "Optional": "False", "Line": 834, "CharPositionInLine": 4, "type": type("translation_type", (object,), {
                    "Line": 834, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "orientation": type("orientation", (object,), {
                "Optional": "False", "Line": 835, "CharPositionInLine": 4, "type": type("orientation_type", (object,), {
                    "Line": 835, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Quaterniond"
                })
            }),
            "cov": type("cov", (object,), {
                "Optional": "False", "Line": 836, "CharPositionInLine": 4, "type": type("cov_type", (object,), {
                    "Line": 836, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix6d"
                })
            })
        }
    })
})

types["Base-TwistWithCovariance-m"] = type("Base-TwistWithCovariance-m", (object,), {
    "Line": 841, "CharPositionInLine": 0, "type": type("Base-TwistWithCovariance-m_type", (object,), {
        "Line": 841, "CharPositionInLine": 31, "kind": "SequenceType", "Children": {
            "vel": type("vel", (object,), {
                "Optional": "False", "Line": 843, "CharPositionInLine": 4, "type": type("vel_type", (object,), {
                    "Line": 843, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "rot": type("rot", (object,), {
                "Optional": "False", "Line": 844, "CharPositionInLine": 4, "type": type("rot_type", (object,), {
                    "Line": 844, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov": type("cov", (object,), {
                "Optional": "False", "Line": 845, "CharPositionInLine": 4, "type": type("cov_type", (object,), {
                    "Line": 845, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix6d"
                })
            })
        }
    })
})

types["Base-Waypoint-m"] = type("Base-Waypoint-m", (object,), {
    "Line": 850, "CharPositionInLine": 0, "type": type("Base-Waypoint-m_type", (object,), {
        "Line": 850, "CharPositionInLine": 20, "kind": "SequenceType", "Children": {
            "position": type("position", (object,), {
                "Optional": "False", "Line": 852, "CharPositionInLine": 4, "type": type("position_type", (object,), {
                    "Line": 852, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "heading": type("heading", (object,), {
                "Optional": "False", "Line": 853, "CharPositionInLine": 4, "type": type("heading_type", (object,), {
                    "Line": 853, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "tol-position": type("tol-position", (object,), {
                "Optional": "False", "Line": 854, "CharPositionInLine": 4, "type": type("tol-position_type", (object,), {
                    "Line": 854, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "tol-heading": type("tol-heading", (object,), {
                "Optional": "False", "Line": 855, "CharPositionInLine": 4, "type": type("tol-heading_type", (object,), {
                    "Line": 855, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            })
        }
    })
})

types["Base-Wrench-m"] = type("Base-Wrench-m", (object,), {
    "Line": 860, "CharPositionInLine": 0, "type": type("Base-Wrench-m_type", (object,), {
        "Line": 860, "CharPositionInLine": 18, "kind": "SequenceType", "Children": {
            "force": type("force", (object,), {
                "Optional": "False", "Line": 862, "CharPositionInLine": 4, "type": type("force_type", (object,), {
                    "Line": 862, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "torque": type("torque", (object,), {
                "Optional": "False", "Line": 863, "CharPositionInLine": 4, "type": type("torque_type", (object,), {
                    "Line": 863, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            })
        }
    })
})

types["Base-commands-LinearAngular6DCommand-m"] = type("Base-commands-LinearAngular6DCommand-m", (object,), {
    "Line": 868, "CharPositionInLine": 0, "type": type("Base-commands-LinearAngular6DCommand-m_type", (object,), {
        "Line": 868, "CharPositionInLine": 43, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 870, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 870, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "linear": type("linear", (object,), {
                "Optional": "False", "Line": 871, "CharPositionInLine": 4, "type": type("linear_type", (object,), {
                    "Line": 871, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "angular": type("angular", (object,), {
                "Optional": "False", "Line": 872, "CharPositionInLine": 4, "type": type("angular_type", (object,), {
                    "Line": 872, "CharPositionInLine": 13, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            })
        }
    })
})

types["Base-samples-BodyState-m"] = type("Base-samples-BodyState-m", (object,), {
    "Line": 877, "CharPositionInLine": 0, "type": type("Base-samples-BodyState-m_type", (object,), {
        "Line": 877, "CharPositionInLine": 29, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 879, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 879, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "pose": type("pose", (object,), {
                "Optional": "False", "Line": 880, "CharPositionInLine": 4, "type": type("pose_type", (object,), {
                    "Line": 880, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-TransformWithCovariance-m"
                })
            }),
            "velocity": type("velocity", (object,), {
                "Optional": "False", "Line": 881, "CharPositionInLine": 4, "type": type("velocity_type", (object,), {
                    "Line": 881, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Base-TwistWithCovariance-m"
                })
            })
        }
    })
})

types["Base-samples-IMUSensors-m"] = type("Base-samples-IMUSensors-m", (object,), {
    "Line": 886, "CharPositionInLine": 0, "type": type("Base-samples-IMUSensors-m_type", (object,), {
        "Line": 886, "CharPositionInLine": 30, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 888, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 888, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "acc": type("acc", (object,), {
                "Optional": "False", "Line": 889, "CharPositionInLine": 4, "type": type("acc_type", (object,), {
                    "Line": 889, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "gyro": type("gyro", (object,), {
                "Optional": "False", "Line": 890, "CharPositionInLine": 4, "type": type("gyro_type", (object,), {
                    "Line": 890, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "mag": type("mag", (object,), {
                "Optional": "False", "Line": 891, "CharPositionInLine": 4, "type": type("mag_type", (object,), {
                    "Line": 891, "CharPositionInLine": 9, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            })
        }
    })
})

types["Base-samples-RigidBodyAcceleration-m"] = type("Base-samples-RigidBodyAcceleration-m", (object,), {
    "Line": 896, "CharPositionInLine": 0, "type": type("Base-samples-RigidBodyAcceleration-m_type", (object,), {
        "Line": 896, "CharPositionInLine": 41, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 898, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 898, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "acceleration": type("acceleration", (object,), {
                "Optional": "False", "Line": 899, "CharPositionInLine": 4, "type": type("acceleration_type", (object,), {
                    "Line": 899, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-acceleration": type("cov-acceleration", (object,), {
                "Optional": "False", "Line": 900, "CharPositionInLine": 4, "type": type("cov-acceleration_type", (object,), {
                    "Line": 900, "CharPositionInLine": 22, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            }),
            "angular-acceleration": type("angular-acceleration", (object,), {
                "Optional": "False", "Line": 901, "CharPositionInLine": 4, "type": type("angular-acceleration_type", (object,), {
                    "Line": 901, "CharPositionInLine": 26, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-angular-acceleration": type("cov-angular-acceleration", (object,), {
                "Optional": "False", "Line": 902, "CharPositionInLine": 4, "type": type("cov-angular-acceleration_type", (object,), {
                    "Line": 902, "CharPositionInLine": 30, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            })
        }
    })
})

types["Base-samples-RigidBodyState-m"] = type("Base-samples-RigidBodyState-m", (object,), {
    "Line": 907, "CharPositionInLine": 0, "type": type("Base-samples-RigidBodyState-m_type", (object,), {
        "Line": 907, "CharPositionInLine": 34, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 909, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 909, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "sourceframe": type("sourceframe", (object,), {
                "Optional": "False", "Line": 910, "CharPositionInLine": 4, "type": type("sourceframe_type", (object,), {
                    "Line": 910, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "targetframe": type("targetframe", (object,), {
                "Optional": "False", "Line": 911, "CharPositionInLine": 4, "type": type("targetframe_type", (object,), {
                    "Line": 911, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "position": type("position", (object,), {
                "Optional": "False", "Line": 912, "CharPositionInLine": 4, "type": type("position_type", (object,), {
                    "Line": 912, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-position": type("cov-position", (object,), {
                "Optional": "False", "Line": 913, "CharPositionInLine": 4, "type": type("cov-position_type", (object,), {
                    "Line": 913, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            }),
            "orientation": type("orientation", (object,), {
                "Optional": "False", "Line": 914, "CharPositionInLine": 4, "type": type("orientation_type", (object,), {
                    "Line": 914, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Quaterniond"
                })
            }),
            "cov-orientation": type("cov-orientation", (object,), {
                "Optional": "False", "Line": 915, "CharPositionInLine": 4, "type": type("cov-orientation_type", (object,), {
                    "Line": 915, "CharPositionInLine": 21, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            }),
            "velocity": type("velocity", (object,), {
                "Optional": "False", "Line": 916, "CharPositionInLine": 4, "type": type("velocity_type", (object,), {
                    "Line": 916, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-velocity": type("cov-velocity", (object,), {
                "Optional": "False", "Line": 917, "CharPositionInLine": 4, "type": type("cov-velocity_type", (object,), {
                    "Line": 917, "CharPositionInLine": 18, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            }),
            "angular-velocity": type("angular-velocity", (object,), {
                "Optional": "False", "Line": 918, "CharPositionInLine": 4, "type": type("angular-velocity_type", (object,), {
                    "Line": 918, "CharPositionInLine": 22, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "cov-angular-velocity": type("cov-angular-velocity", (object,), {
                "Optional": "False", "Line": 919, "CharPositionInLine": 4, "type": type("cov-angular-velocity_type", (object,), {
                    "Line": 919, "CharPositionInLine": 26, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Matrix3d"
                })
            })
        }
    })
})

types["Base-samples-Wrench-m"] = type("Base-samples-Wrench-m", (object,), {
    "Line": 924, "CharPositionInLine": 0, "type": type("Base-samples-Wrench-m_type", (object,), {
        "Line": 924, "CharPositionInLine": 26, "kind": "SequenceType", "Children": {
            "force": type("force", (object,), {
                "Optional": "False", "Line": 926, "CharPositionInLine": 4, "type": type("force_type", (object,), {
                    "Line": 926, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "torque": type("torque", (object,), {
                "Optional": "False", "Line": 927, "CharPositionInLine": 4, "type": type("torque_type", (object,), {
                    "Line": 927, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
                })
            }),
            "time": type("time", (object,), {
                "Optional": "False", "Line": 928, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 928, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            })
        }
    })
})

types["Base-JointTransformVector-m"] = type("Base-JointTransformVector-m", (object,), {
    "Line": 941, "CharPositionInLine": 0, "type": type("Base-JointTransformVector-m_type", (object,), {
        "Line": 933, "CharPositionInLine": 81, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 935, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTransformVector-m-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 936, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 936, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Std-orogen-typekits-mtype-std-vector-base-JointTransform", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-NamedVector-base-JointTransform-m"] = type("Base-NamedVector-base-JointTransform-m", (object,), {
    "Line": 953, "CharPositionInLine": 0, "type": type("Base-NamedVector-base-JointTransform-m_type", (object,), {
        "Line": 945, "CharPositionInLine": 103, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 947, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-base-JointTransform-m-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 948, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 948, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Std-orogen-typekits-mtype-std-vector-base-JointTransform", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-NamedVector-base-Wrench-m"] = type("Base-NamedVector-base-Wrench-m", (object,), {
    "Line": 965, "CharPositionInLine": 0, "type": type("Base-NamedVector-base-Wrench-m_type", (object,), {
        "Line": 957, "CharPositionInLine": 87, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 959, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-NamedVector-base-Wrench-m-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 960, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 960, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Std-orogen-typekits-mtype-std-vector-base-Wrench", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-samples-Pointcloud-m"] = type("Base-samples-Pointcloud-m", (object,), {
    "Line": 978, "CharPositionInLine": 0, "type": type("Base-samples-Pointcloud-m_type", (object,), {
        "Line": 969, "CharPositionInLine": 125, "kind": "SequenceType", "Children": {
            "time": type("time", (object,), {
                "Optional": "False", "Line": 971, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 971, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            }),
            "points": type("points", (object,), {
                "Optional": "False", "Line": 972, "CharPositionInLine": 4, "type": type("points_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Pointcloud-m-points", "Min": "1", "Max": "200"
                })
            }),
            "colors": type("colors", (object,), {
                "Optional": "False", "Line": 973, "CharPositionInLine": 4, "type": type("colors_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Pointcloud-m-colors", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-samples-Wrenches-m"] = type("Base-samples-Wrenches-m", (object,), {
    "Line": 991, "CharPositionInLine": 0, "type": type("Base-samples-Wrenches-m_type", (object,), {
        "Line": 982, "CharPositionInLine": 73, "kind": "SequenceType", "Children": {
            "names": type("names", (object,), {
                "Optional": "False", "Line": 984, "CharPositionInLine": 4, "type": type("names_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-Wrenches-m-names", "Min": "1", "Max": "200"
                })
            }),
            "elements": type("elements", (object,), {
                "Optional": "False", "Line": 985, "CharPositionInLine": 4, "type": type("elements_type", (object,), {
                    "Line": 985, "CharPositionInLine": 14, "kind": "ReferenceType", "ReferencedTypeName": "Std-orogen-typekits-mtype-std-vector-base-Wrench", "Min": "1", "Max": "200"
                })
            }),
            "time": type("time", (object,), {
                "Optional": "False", "Line": 986, "CharPositionInLine": 4, "type": type("time_type", (object,), {
                    "Line": 986, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
                })
            })
        }
    })
})

types["Wrappers-geometry-Spline"] = type("Wrappers-geometry-Spline", (object,), {
    "Line": 1007, "CharPositionInLine": 0, "type": type("Wrappers-geometry-Spline_type", (object,), {
        "Line": 995, "CharPositionInLine": 123, "kind": "SequenceType", "Children": {
            "geometric-resolution": type("geometric-resolution", (object,), {
                "Optional": "False", "Line": 997, "CharPositionInLine": 4, "type": type("geometric-resolution_type", (object,), {
                    "Line": 997, "CharPositionInLine": 26, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "dimension": type("dimension", (object,), {
                "Optional": "False", "Line": 998, "CharPositionInLine": 4, "type": type("dimension_type", (object,), {
                    "Line": 998, "CharPositionInLine": 15, "kind": "ReferenceType", "ReferencedTypeName": "T-Int32", "Min": "-2147483648", "Max": "2147483647", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "curve-order": type("curve-order", (object,), {
                "Optional": "False", "Line": 999, "CharPositionInLine": 4, "type": type("curve-order_type", (object,), {
                    "Line": 999, "CharPositionInLine": 17, "kind": "ReferenceType", "ReferencedTypeName": "T-Int32", "Min": "-2147483648", "Max": "2147483647", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "kind": type("kind", (object,), {
                "Optional": "False", "Line": 1000, "CharPositionInLine": 4, "type": type("kind_type", (object,), {
                    "Line": 1000, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-geometry-SplineType"
                })
            }),
            "knots": type("knots", (object,), {
                "Optional": "False", "Line": 1001, "CharPositionInLine": 4, "type": type("knots_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-geometry-Spline-knots", "Min": "1", "Max": "200"
                })
            }),
            "vertices": type("vertices", (object,), {
                "Optional": "False", "Line": 1002, "CharPositionInLine": 4, "type": type("vertices_type", (object,), {
                    "Line": 0, "CharPositionInLine": 0, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-geometry-Spline-vertices", "Min": "1", "Max": "200"
                })
            })
        }
    })
})

types["Base-Trajectory-m"] = type("Base-Trajectory-m", (object,), {
    "Line": 1011, "CharPositionInLine": 0, "type": type("Base-Trajectory-m_type", (object,), {
        "Line": 1011, "CharPositionInLine": 22, "kind": "SequenceType", "Children": {
            "speed": type("speed", (object,), {
                "Optional": "False", "Line": 1013, "CharPositionInLine": 4, "type": type("speed_type", (object,), {
                    "Line": 1013, "CharPositionInLine": 11, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
                })
            }),
            "spline": type("spline", (object,), {
                "Optional": "False", "Line": 1014, "CharPositionInLine": 4, "type": type("spline_type", (object,), {
                    "Line": 1014, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-geometry-Spline"
                })
            })
        }
    })
})

types["Wrappers-geometry-Spline-vertices"] = type("Wrappers-geometry-Spline-vertices", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-geometry-Spline-vertices_type", (object,), {
        "Line": 1002, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 1002, "CharPositionInLine": 74, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-geometry-Spline-knots"] = type("Wrappers-geometry-Spline-knots", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-geometry-Spline-knots_type", (object,), {
        "Line": 1001, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 1001, "CharPositionInLine": 68, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-Wrenches-m-names"] = type("Base-samples-Wrenches-m-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Wrenches-m-names_type", (object,), {
        "Line": 984, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 984, "CharPositionInLine": 67, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-Pointcloud-m-colors"] = type("Base-samples-Pointcloud-m-colors", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Pointcloud-m-colors_type", (object,), {
        "Line": 973, "CharPositionInLine": 12, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 973, "CharPositionInLine": 71, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector4d"
        })
    })
})

types["Base-samples-Pointcloud-m-points"] = type("Base-samples-Pointcloud-m-points", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Pointcloud-m-points_type", (object,), {
        "Line": 972, "CharPositionInLine": 12, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 972, "CharPositionInLine": 71, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
        })
    })
})

types["Base-NamedVector-base-Wrench-m-names"] = type("Base-NamedVector-base-Wrench-m-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-base-Wrench-m-names_type", (object,), {
        "Line": 959, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 959, "CharPositionInLine": 74, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-NamedVector-base-JointTransform-m-names"] = type("Base-NamedVector-base-JointTransform-m-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-base-JointTransform-m-names_type", (object,), {
        "Line": 947, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 947, "CharPositionInLine": 82, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-JointTransformVector-m-names"] = type("Base-JointTransformVector-m-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-JointTransformVector-m-names_type", (object,), {
        "Line": 935, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 935, "CharPositionInLine": 71, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-VectorXd-data"] = type("Wrappers-VectorXd-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-VectorXd-data_type", (object,), {
        "Line": 798, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 798, "CharPositionInLine": 59, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-Quaterniond-im"] = type("Wrappers-Quaterniond-im", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-Quaterniond-im_type", (object,), {
        "Line": 790, "CharPositionInLine": 8, "kind": "SequenceOfType", "Min": "1", "Max": "3", "type": type("SeqOf_type", (object,), {
            "Line": 790, "CharPositionInLine": 32, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-MatrixXd-data"] = type("Wrappers-MatrixXd-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-MatrixXd-data_type", (object,), {
        "Line": 779, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 779, "CharPositionInLine": 59, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-Matrix6d-data"] = type("Wrappers-Matrix6d-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-Matrix6d-data_type", (object,), {
        "Line": 770, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "36", "type": type("SeqOf_type", (object,), {
            "Line": 770, "CharPositionInLine": 35, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-Vector6d-data"] = type("Wrappers-Vector6d-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-Vector6d-data_type", (object,), {
        "Line": 763, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "6", "type": type("SeqOf_type", (object,), {
            "Line": 763, "CharPositionInLine": 34, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-Matrix4d-data"] = type("Wrappers-Matrix4d-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-Matrix4d-data_type", (object,), {
        "Line": 756, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "16", "type": type("SeqOf_type", (object,), {
            "Line": 756, "CharPositionInLine": 35, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-Vector4d-data"] = type("Wrappers-Vector4d-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-Vector4d-data_type", (object,), {
        "Line": 749, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "4", "type": type("SeqOf_type", (object,), {
            "Line": 749, "CharPositionInLine": 34, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-Matrix3d-data"] = type("Wrappers-Matrix3d-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-Matrix3d-data_type", (object,), {
        "Line": 742, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "9", "type": type("SeqOf_type", (object,), {
            "Line": 742, "CharPositionInLine": 34, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-Vector3d-data"] = type("Wrappers-Vector3d-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-Vector3d-data_type", (object,), {
        "Line": 735, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "3", "type": type("SeqOf_type", (object,), {
            "Line": 735, "CharPositionInLine": 34, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-Matrix2d-data"] = type("Wrappers-Matrix2d-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-Matrix2d-data_type", (object,), {
        "Line": 728, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "4", "type": type("SeqOf_type", (object,), {
            "Line": 728, "CharPositionInLine": 34, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-Vector2d-data"] = type("Wrappers-Vector2d-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-Vector2d-data_type", (object,), {
        "Line": 721, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "2", "type": type("SeqOf_type", (object,), {
            "Line": 721, "CharPositionInLine": 34, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Wrappers-AngleAxisd-axis"] = type("Wrappers-AngleAxisd-axis", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Wrappers-AngleAxisd-axis_type", (object,), {
        "Line": 714, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "3", "type": type("SeqOf_type", (object,), {
            "Line": 714, "CharPositionInLine": 34, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-frame-Frame-attributes"] = type("Base-samples-frame-Frame-attributes", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-frame-Frame-attributes_type", (object,), {
        "Line": 686, "CharPositionInLine": 16, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 686, "CharPositionInLine": 78, "kind": "ReferenceType", "ReferencedTypeName": "Base-samples-frame-frame-attrib-t"
        })
    })
})

types["Base-samples-frame-Frame-image"] = type("Base-samples-frame-Frame-image", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-frame-Frame-image_type", (object,), {
        "Line": 685, "CharPositionInLine": 11, "kind": "OctetStringType", "Min": "1", "Max": "200"
    })
})

types["Base-NamedVector-Base-JointTransform-elements"] = type("Base-NamedVector-Base-JointTransform-elements", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointTransform-elements_type", (object,), {
        "Line": 672, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 672, "CharPositionInLine": 86, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTransform"
        })
    })
})

types["Base-NamedVector-Base-JointTransform-names"] = type("Base-NamedVector-Base-JointTransform-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointTransform-names_type", (object,), {
        "Line": 671, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 671, "CharPositionInLine": 80, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-JointTransformVector-elements"] = type("Base-JointTransformVector-elements", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-JointTransformVector-elements_type", (object,), {
        "Line": 660, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 660, "CharPositionInLine": 75, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTransform"
        })
    })
})

types["Base-JointTransformVector-names"] = type("Base-JointTransformVector-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-JointTransformVector-names_type", (object,), {
        "Line": 659, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 659, "CharPositionInLine": 69, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-Wrenches-elements"] = type("Base-samples-Wrenches-elements", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Wrenches-elements_type", (object,), {
        "Line": 639, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 639, "CharPositionInLine": 71, "kind": "ReferenceType", "ReferencedTypeName": "Base-Wrench"
        })
    })
})

types["Base-samples-Wrenches-names"] = type("Base-samples-Wrenches-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Wrenches-names_type", (object,), {
        "Line": 638, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 638, "CharPositionInLine": 65, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-SonarScan-time-beams"] = type("Base-samples-SonarScan-time-beams", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-SonarScan-time-beams_type", (object,), {
        "Line": 617, "CharPositionInLine": 16, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 617, "CharPositionInLine": 76, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
        })
    })
})

types["Base-samples-SonarScan-data"] = type("Base-samples-SonarScan-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-SonarScan-data_type", (object,), {
        "Line": 616, "CharPositionInLine": 10, "kind": "OctetStringType", "Min": "1", "Max": "200"
    })
})

types["Base-samples-SonarBeam-beam"] = type("Base-samples-SonarBeam-beam", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-SonarBeam-beam_type", (object,), {
        "Line": 604, "CharPositionInLine": 10, "kind": "OctetStringType", "Min": "1", "Max": "200"
    })
})

types["Base-samples-Sonar-bins"] = type("Base-samples-Sonar-bins", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Sonar-bins_type", (object,), {
        "Line": 587, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 587, "CharPositionInLine": 60, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-Sonar-bearings"] = type("Base-samples-Sonar-bearings", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Sonar-bearings_type", (object,), {
        "Line": 583, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 583, "CharPositionInLine": 68, "kind": "ReferenceType", "ReferencedTypeName": "Base-Angle"
        })
    })
})

types["Base-samples-Sonar-timestamps"] = type("Base-samples-Sonar-timestamps", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Sonar-timestamps_type", (object,), {
        "Line": 579, "CharPositionInLine": 16, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 579, "CharPositionInLine": 72, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
        })
    })
})

types["Base-samples-Pointcloud-colors"] = type("Base-samples-Pointcloud-colors", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Pointcloud-colors_type", (object,), {
        "Line": 550, "CharPositionInLine": 12, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 550, "CharPositionInLine": 69, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector4d"
        })
    })
})

types["Base-samples-Pointcloud-points"] = type("Base-samples-Pointcloud-points", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-Pointcloud-points_type", (object,), {
        "Line": 549, "CharPositionInLine": 12, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 549, "CharPositionInLine": 69, "kind": "ReferenceType", "ReferencedTypeName": "Wrappers-Vector3d"
        })
    })
})

types["Base-samples-LaserScan-remission"] = type("Base-samples-LaserScan-remission", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-LaserScan-remission_type", (object,), {
        "Line": 537, "CharPositionInLine": 15, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 537, "CharPositionInLine": 74, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-LaserScan-ranges"] = type("Base-samples-LaserScan-ranges", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-LaserScan-ranges_type", (object,), {
        "Line": 534, "CharPositionInLine": 12, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 534, "CharPositionInLine": 68, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
        })
    })
})

types["Base-commands-Joints-names"] = type("Base-commands-Joints-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-commands-Joints-names_type", (object,), {
        "Line": 517, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 517, "CharPositionInLine": 64, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-DistanceImage-data"] = type("Base-samples-DistanceImage-data", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-DistanceImage-data_type", (object,), {
        "Line": 506, "CharPositionInLine": 10, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 506, "CharPositionInLine": 68, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-DepthMap-remissions"] = type("Base-samples-DepthMap-remissions", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-DepthMap-remissions_type", (object,), {
        "Line": 488, "CharPositionInLine": 16, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 488, "CharPositionInLine": 75, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-DepthMap-distances"] = type("Base-samples-DepthMap-distances", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-DepthMap-distances_type", (object,), {
        "Line": 487, "CharPositionInLine": 15, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 487, "CharPositionInLine": 73, "kind": "ReferenceType", "ReferencedTypeName": "T-Float", "Min": "-3.402823466E+38", "Max": "3.402823466E+38", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-DepthMap-horizontal-interval"] = type("Base-samples-DepthMap-horizontal-interval", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-DepthMap-horizontal-interval_type", (object,), {
        "Line": 484, "CharPositionInLine": 25, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 484, "CharPositionInLine": 93, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-DepthMap-vertical-interval"] = type("Base-samples-DepthMap-vertical-interval", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-DepthMap-vertical-interval_type", (object,), {
        "Line": 483, "CharPositionInLine": 23, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 483, "CharPositionInLine": 89, "kind": "ReferenceType", "ReferencedTypeName": "T-Double", "Min": "-1.79769313486232E+308", "Max": "1.79769313486232E+308", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-samples-DepthMap-timestamps"] = type("Base-samples-DepthMap-timestamps", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-samples-DepthMap-timestamps_type", (object,), {
        "Line": 480, "CharPositionInLine": 16, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 480, "CharPositionInLine": 75, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
        })
    })
})

types["Base-NamedVector-Base-JointTrajectory-elements"] = type("Base-NamedVector-Base-JointTrajectory-elements", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointTrajectory-elements_type", (object,), {
        "Line": 468, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 468, "CharPositionInLine": 87, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTrajectory", "Min": "1", "Max": "200"
        })
    })
})

types["Base-NamedVector-Base-JointTrajectory-names"] = type("Base-NamedVector-Base-JointTrajectory-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointTrajectory-names_type", (object,), {
        "Line": 467, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 467, "CharPositionInLine": 81, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-NamedVector-Base-Wrench-elements"] = type("Base-NamedVector-Base-Wrench-elements", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-Wrench-elements_type", (object,), {
        "Line": 456, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 456, "CharPositionInLine": 78, "kind": "ReferenceType", "ReferencedTypeName": "Base-Wrench"
        })
    })
})

types["Base-NamedVector-Base-Wrench-names"] = type("Base-NamedVector-Base-Wrench-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-Wrench-names_type", (object,), {
        "Line": 455, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 455, "CharPositionInLine": 72, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-NamedVector-Base-JointState-names"] = type("Base-NamedVector-Base-JointState-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointState-names_type", (object,), {
        "Line": 443, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 443, "CharPositionInLine": 76, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-NamedVector-Base-JointLimitRange-elements"] = type("Base-NamedVector-Base-JointLimitRange-elements", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointLimitRange-elements_type", (object,), {
        "Line": 432, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 432, "CharPositionInLine": 87, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointLimitRange"
        })
    })
})

types["Base-NamedVector-Base-JointLimitRange-names"] = type("Base-NamedVector-Base-JointLimitRange-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-NamedVector-Base-JointLimitRange-names_type", (object,), {
        "Line": 431, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 431, "CharPositionInLine": 81, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-JointsTrajectory-times-val"] = type("Base-JointsTrajectory-times-val", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-JointsTrajectory-times-val_type", (object,), {
        "Line": 420, "CharPositionInLine": 15, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 420, "CharPositionInLine": 73, "kind": "ReferenceType", "ReferencedTypeName": "Base-Time"
        })
    })
})

types["Base-JointsTrajectory-elements"] = type("Base-JointsTrajectory-elements", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-JointsTrajectory-elements_type", (object,), {
        "Line": 419, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 419, "CharPositionInLine": 71, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointTrajectory", "Min": "1", "Max": "200"
        })
    })
})

types["Base-JointsTrajectory-names"] = type("Base-JointsTrajectory-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-JointsTrajectory-names_type", (object,), {
        "Line": 418, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 418, "CharPositionInLine": 65, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})

types["Base-JointLimits-elements"] = type("Base-JointLimits-elements", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-JointLimits-elements_type", (object,), {
        "Line": 398, "CharPositionInLine": 14, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 398, "CharPositionInLine": 66, "kind": "ReferenceType", "ReferencedTypeName": "Base-JointLimitRange"
        })
    })
})

types["Base-JointLimits-names"] = type("Base-JointLimits-names", (object,), {
    "Line": 0, "CharPositionInLine": 0, "type": type("Base-JointLimits-names_type", (object,), {
        "Line": 397, "CharPositionInLine": 11, "kind": "SequenceOfType", "Min": "1", "Max": "200", "type": type("SeqOf_type", (object,), {
            "Line": 397, "CharPositionInLine": 60, "kind": "ReferenceType", "ReferencedTypeName": "T-String", "Min": "0", "Max": "60", "ReferencedModName": "TASTE-ExtendedTypes"
        })
    })
})



asn1Modules.append("TASTE-ExtendedTypes")
exportedTypes["TASTE-ExtendedTypes"] = ["T-Double", "T-Float", "T-Int16", "T-UInt16", "T-UInt64", "T-Int64", "T-String", "T-Time", "T-Int32", "T-UInt32", "T-Int8", "T-UInt8", "T-Boolean"]
exportedVariables["TASTE-ExtendedTypes"] = ["numT-String"]
importedModules["TASTE-ExtendedTypes"] = [{"TASTE-BasicTypes":{"ImportedTypes": ["T-Int32","T-UInt32","T-Int8","T-UInt8","T-Boolean"], "ImportedVariables": []}}]

types["T-Double"] = type("T-Double", (object,), {
    "Line": 1028, "CharPositionInLine": 0, "type": type("T-Double_type", (object,), {
        "Line": 1028, "CharPositionInLine": 13, "kind": "RealType", "Min": "-1.79769313486231570000E+308", "Max": "1.79769313486231570000E+308"
    })
})

types["T-Float"] = type("T-Float", (object,), {
    "Line": 1030, "CharPositionInLine": 0, "type": type("T-Float_type", (object,), {
        "Line": 1030, "CharPositionInLine": 12, "kind": "RealType", "Min": "-3.40282346600000020000E+038", "Max": "3.40282346600000020000E+038"
    })
})

types["T-Int16"] = type("T-Int16", (object,), {
    "Line": 1032, "CharPositionInLine": 0, "type": type("T-Int16_type", (object,), {
        "Line": 1032, "CharPositionInLine": 12, "kind": "IntegerType", "Min": "-32768", "Max": "32767"
    })
})

types["T-UInt16"] = type("T-UInt16", (object,), {
    "Line": 1034, "CharPositionInLine": 0, "type": type("T-UInt16_type", (object,), {
        "Line": 1034, "CharPositionInLine": 13, "kind": "IntegerType", "Min": "0", "Max": "65535"
    })
})

types["T-UInt64"] = type("T-UInt64", (object,), {
    "Line": 1036, "CharPositionInLine": 0, "type": type("T-UInt64_type", (object,), {
        "Line": 1036, "CharPositionInLine": 13, "kind": "IntegerType", "Min": "0", "Max": "9223372036854775807"
    })
})

types["T-Int64"] = type("T-Int64", (object,), {
    "Line": 1038, "CharPositionInLine": 0, "type": type("T-Int64_type", (object,), {
        "Line": 1038, "CharPositionInLine": 12, "kind": "IntegerType", "Min": "-9223372036854775807", "Max": "9223372036854775807"
    })
})

types["T-String"] = type("T-String", (object,), {
    "Line": 1040, "CharPositionInLine": 0, "type": type("T-String_type", (object,), {
        "Line": 1042, "CharPositionInLine": 37, "kind": "OctetStringType", "Min": "0", "Max": "60"
    })
})

types["T-Time"] = type("T-Time", (object,), {
    "Line": 1046, "CharPositionInLine": 0, "type": type("T-Time_type", (object,), {
        "Line": 1046, "CharPositionInLine": 11, "kind": "SequenceType", "Children": {
            "secs": type("secs", (object,), {
                "Optional": "False", "Line": 1048, "CharPositionInLine": 4, "type": type("secs_type", (object,), {
                    "Line": 1048, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            }),
            "nsecs": type("nsecs", (object,), {
                "Optional": "False", "Line": 1049, "CharPositionInLine": 4, "type": type("nsecs_type", (object,), {
                    "Line": 1049, "CharPositionInLine": 10, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
                })
            })
        }
    })
})


variables["numT-String"] = type("numT-String", (object,), {
    "Line": 1044,
    "CharPositionInLine": 0,
    "varName": "numT_String",
    "type": type("numT-String_type", (object,), {
        "Line": 1044, "CharPositionInLine": 12, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 60
})

asn1Modules.append("TASTE-BasicTypes")
exportedTypes["TASTE-BasicTypes"] = ["T-Int32", "T-UInt32", "T-Int8", "T-UInt8", "T-Boolean"]
exportedVariables["TASTE-BasicTypes"] = []
importedModules["TASTE-BasicTypes"] = []

types["T-Int32"] = type("T-Int32", (object,), {
    "Line": 1059, "CharPositionInLine": 0, "type": type("T-Int32_type", (object,), {
        "Line": 1059, "CharPositionInLine": 13, "kind": "IntegerType", "Min": "-2147483648", "Max": "2147483647"
    })
})

types["T-UInt32"] = type("T-UInt32", (object,), {
    "Line": 1061, "CharPositionInLine": 0, "type": type("T-UInt32_type", (object,), {
        "Line": 1061, "CharPositionInLine": 13, "kind": "IntegerType", "Min": "0", "Max": "4294967295"
    })
})

types["T-Int8"] = type("T-Int8", (object,), {
    "Line": 1063, "CharPositionInLine": 0, "type": type("T-Int8_type", (object,), {
        "Line": 1063, "CharPositionInLine": 11, "kind": "IntegerType", "Min": "-128", "Max": "127"
    })
})

types["T-UInt8"] = type("T-UInt8", (object,), {
    "Line": 1065, "CharPositionInLine": 0, "type": type("T-UInt8_type", (object,), {
        "Line": 1065, "CharPositionInLine": 12, "kind": "IntegerType", "Min": "0", "Max": "255"
    })
})

types["T-Boolean"] = type("T-Boolean", (object,), {
    "Line": 1067, "CharPositionInLine": 0, "type": type("T-Boolean_type", (object,), {
        "Line": 1067, "CharPositionInLine": 14, "kind": "BooleanType"
    })
})



asn1Modules.append("UserDefs-Base-Types")
exportedTypes["UserDefs-Base-Types"] = ["DummyBase-T", "T-UInt32"]
exportedVariables["UserDefs-Base-Types"] = ["numBase-JointTrajectory", "numStd-orogen-typekits-mtype-std-vector-base-JointTransform", "numStd-orogen-typekits-mtype-std-vector-base-Waypoint", "numStd-orogen-typekits-mtype-std-vector-base-Wrench", "numStd-vector-Wrappers-Vector4d", "numStd-orogen-typekits-mtype-std-vector-base-Trajectory", "numBase-JointLimits-names", "numBase-JointLimits-elements", "numBase-JointsTrajectory-names", "numBase-JointsTrajectory-elements", "numBase-JointsTrajectory-times-val", "numBase-NamedVector-Base-JointLimitRange-names", "numBase-NamedVector-Base-JointLimitRange-elements", "numBase-NamedVector-Base-JointState-names", "numBase-NamedVector-Base-Wrench-names", "numBase-NamedVector-Base-Wrench-elements", "numBase-NamedVector-Base-JointTrajectory-names", "numBase-NamedVector-Base-JointTrajectory-elements", "numBase-samples-DepthMap-timestamps", "numBase-samples-DepthMap-vertical-interval", "numBase-samples-DepthMap-horizontal-interval", "numBase-samples-DepthMap-distances", "numBase-samples-DepthMap-remissions", "numBase-samples-DistanceImage-data", "numBase-commands-Joints-names", "numBase-samples-LaserScan-ranges", "numBase-samples-LaserScan-remission", "numBase-samples-Pointcloud-points", "numBase-samples-Pointcloud-colors", "numBase-samples-Sonar-timestamps", "numBase-samples-Sonar-bearings", "numBase-samples-Sonar-bins", "numBase-samples-SonarBeam-beam", "numBase-samples-SonarScan-data", "numBase-samples-SonarScan-time-beams", "numBase-samples-Wrenches-names", "numBase-samples-Wrenches-elements", "numBase-JointTransformVector-names", "numBase-JointTransformVector-elements", "numBase-NamedVector-Base-JointTransform-names", "numBase-NamedVector-Base-JointTransform-elements", "numBase-samples-frame-Frame-image", "numBase-samples-frame-Frame-attributes", "numWrappers-MatrixXd-data", "numWrappers-VectorXd-data", "numBase-JointTransformVector-m-names", "numBase-NamedVector-base-JointTransform-m-names", "numBase-NamedVector-base-Wrench-m-names", "numBase-samples-Pointcloud-m-points", "numBase-samples-Pointcloud-m-colors", "numBase-samples-Wrenches-m-names", "numWrappers-geometry-Spline-knots", "numWrappers-geometry-Spline-vertices"]
importedModules["UserDefs-Base-Types"] = [{"TASTE-BasicTypes":{"ImportedTypes": ["T-UInt32"], "ImportedVariables": []}}]

types["DummyBase-T"] = type("DummyBase-T", (object,), {
    "Line": 1077, "CharPositionInLine": 4, "type": type("DummyBase-T_type", (object,), {
        "Line": 1077, "CharPositionInLine": 20, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    })
})


variables["numBase-JointTrajectory"] = type("numBase-JointTrajectory", (object,), {
    "Line": 1081,
    "CharPositionInLine": 4,
    "varName": "numBase_JointTrajectory",
    "type": type("numBase-JointTrajectory_type", (object,), {
        "Line": 1081, "CharPositionInLine": 28, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numStd-orogen-typekits-mtype-std-vector-base-JointTransform"] = type("numStd-orogen-typekits-mtype-std-vector-base-JointTransform", (object,), {
    "Line": 1085,
    "CharPositionInLine": 4,
    "varName": "numStd_orogen_typekits_mtype_std_vector_base_JointTransform",
    "type": type("numStd-orogen-typekits-mtype-std-vector-base-JointTransform_type", (object,), {
        "Line": 1085, "CharPositionInLine": 64, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numStd-orogen-typekits-mtype-std-vector-base-Waypoint"] = type("numStd-orogen-typekits-mtype-std-vector-base-Waypoint", (object,), {
    "Line": 1089,
    "CharPositionInLine": 4,
    "varName": "numStd_orogen_typekits_mtype_std_vector_base_Waypoint",
    "type": type("numStd-orogen-typekits-mtype-std-vector-base-Waypoint_type", (object,), {
        "Line": 1089, "CharPositionInLine": 58, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numStd-orogen-typekits-mtype-std-vector-base-Wrench"] = type("numStd-orogen-typekits-mtype-std-vector-base-Wrench", (object,), {
    "Line": 1093,
    "CharPositionInLine": 4,
    "varName": "numStd_orogen_typekits_mtype_std_vector_base_Wrench",
    "type": type("numStd-orogen-typekits-mtype-std-vector-base-Wrench_type", (object,), {
        "Line": 1093, "CharPositionInLine": 56, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numStd-vector-Wrappers-Vector4d"] = type("numStd-vector-Wrappers-Vector4d", (object,), {
    "Line": 1097,
    "CharPositionInLine": 4,
    "varName": "numStd_vector_Wrappers_Vector4d",
    "type": type("numStd-vector-Wrappers-Vector4d_type", (object,), {
        "Line": 1097, "CharPositionInLine": 36, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numStd-orogen-typekits-mtype-std-vector-base-Trajectory"] = type("numStd-orogen-typekits-mtype-std-vector-base-Trajectory", (object,), {
    "Line": 1101,
    "CharPositionInLine": 4,
    "varName": "numStd_orogen_typekits_mtype_std_vector_base_Trajectory",
    "type": type("numStd-orogen-typekits-mtype-std-vector-base-Trajectory_type", (object,), {
        "Line": 1101, "CharPositionInLine": 60, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-JointLimits-names"] = type("numBase-JointLimits-names", (object,), {
    "Line": 1105,
    "CharPositionInLine": 4,
    "varName": "numBase_JointLimits_names",
    "type": type("numBase-JointLimits-names_type", (object,), {
        "Line": 1105, "CharPositionInLine": 30, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-JointLimits-elements"] = type("numBase-JointLimits-elements", (object,), {
    "Line": 1109,
    "CharPositionInLine": 4,
    "varName": "numBase_JointLimits_elements",
    "type": type("numBase-JointLimits-elements_type", (object,), {
        "Line": 1109, "CharPositionInLine": 33, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-JointsTrajectory-names"] = type("numBase-JointsTrajectory-names", (object,), {
    "Line": 1113,
    "CharPositionInLine": 4,
    "varName": "numBase_JointsTrajectory_names",
    "type": type("numBase-JointsTrajectory-names_type", (object,), {
        "Line": 1113, "CharPositionInLine": 35, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-JointsTrajectory-elements"] = type("numBase-JointsTrajectory-elements", (object,), {
    "Line": 1117,
    "CharPositionInLine": 4,
    "varName": "numBase_JointsTrajectory_elements",
    "type": type("numBase-JointsTrajectory-elements_type", (object,), {
        "Line": 1117, "CharPositionInLine": 38, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-JointsTrajectory-times-val"] = type("numBase-JointsTrajectory-times-val", (object,), {
    "Line": 1121,
    "CharPositionInLine": 4,
    "varName": "numBase_JointsTrajectory_times_val",
    "type": type("numBase-JointsTrajectory-times-val_type", (object,), {
        "Line": 1121, "CharPositionInLine": 39, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-Base-JointLimitRange-names"] = type("numBase-NamedVector-Base-JointLimitRange-names", (object,), {
    "Line": 1125,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_Base_JointLimitRange_names",
    "type": type("numBase-NamedVector-Base-JointLimitRange-names_type", (object,), {
        "Line": 1125, "CharPositionInLine": 51, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-Base-JointLimitRange-elements"] = type("numBase-NamedVector-Base-JointLimitRange-elements", (object,), {
    "Line": 1129,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_Base_JointLimitRange_elements",
    "type": type("numBase-NamedVector-Base-JointLimitRange-elements_type", (object,), {
        "Line": 1129, "CharPositionInLine": 54, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-Base-JointState-names"] = type("numBase-NamedVector-Base-JointState-names", (object,), {
    "Line": 1133,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_Base_JointState_names",
    "type": type("numBase-NamedVector-Base-JointState-names_type", (object,), {
        "Line": 1133, "CharPositionInLine": 46, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-Base-Wrench-names"] = type("numBase-NamedVector-Base-Wrench-names", (object,), {
    "Line": 1137,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_Base_Wrench_names",
    "type": type("numBase-NamedVector-Base-Wrench-names_type", (object,), {
        "Line": 1137, "CharPositionInLine": 42, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-Base-Wrench-elements"] = type("numBase-NamedVector-Base-Wrench-elements", (object,), {
    "Line": 1141,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_Base_Wrench_elements",
    "type": type("numBase-NamedVector-Base-Wrench-elements_type", (object,), {
        "Line": 1141, "CharPositionInLine": 45, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-Base-JointTrajectory-names"] = type("numBase-NamedVector-Base-JointTrajectory-names", (object,), {
    "Line": 1145,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_Base_JointTrajectory_names",
    "type": type("numBase-NamedVector-Base-JointTrajectory-names_type", (object,), {
        "Line": 1145, "CharPositionInLine": 51, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-Base-JointTrajectory-elements"] = type("numBase-NamedVector-Base-JointTrajectory-elements", (object,), {
    "Line": 1149,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_Base_JointTrajectory_elements",
    "type": type("numBase-NamedVector-Base-JointTrajectory-elements_type", (object,), {
        "Line": 1149, "CharPositionInLine": 54, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-DepthMap-timestamps"] = type("numBase-samples-DepthMap-timestamps", (object,), {
    "Line": 1153,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_DepthMap_timestamps",
    "type": type("numBase-samples-DepthMap-timestamps_type", (object,), {
        "Line": 1153, "CharPositionInLine": 40, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-DepthMap-vertical-interval"] = type("numBase-samples-DepthMap-vertical-interval", (object,), {
    "Line": 1157,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_DepthMap_vertical_interval",
    "type": type("numBase-samples-DepthMap-vertical-interval_type", (object,), {
        "Line": 1157, "CharPositionInLine": 47, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-DepthMap-horizontal-interval"] = type("numBase-samples-DepthMap-horizontal-interval", (object,), {
    "Line": 1161,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_DepthMap_horizontal_interval",
    "type": type("numBase-samples-DepthMap-horizontal-interval_type", (object,), {
        "Line": 1161, "CharPositionInLine": 49, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-DepthMap-distances"] = type("numBase-samples-DepthMap-distances", (object,), {
    "Line": 1165,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_DepthMap_distances",
    "type": type("numBase-samples-DepthMap-distances_type", (object,), {
        "Line": 1165, "CharPositionInLine": 39, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-DepthMap-remissions"] = type("numBase-samples-DepthMap-remissions", (object,), {
    "Line": 1169,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_DepthMap_remissions",
    "type": type("numBase-samples-DepthMap-remissions_type", (object,), {
        "Line": 1169, "CharPositionInLine": 40, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-DistanceImage-data"] = type("numBase-samples-DistanceImage-data", (object,), {
    "Line": 1173,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_DistanceImage_data",
    "type": type("numBase-samples-DistanceImage-data_type", (object,), {
        "Line": 1173, "CharPositionInLine": 39, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-commands-Joints-names"] = type("numBase-commands-Joints-names", (object,), {
    "Line": 1177,
    "CharPositionInLine": 4,
    "varName": "numBase_commands_Joints_names",
    "type": type("numBase-commands-Joints-names_type", (object,), {
        "Line": 1177, "CharPositionInLine": 34, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-LaserScan-ranges"] = type("numBase-samples-LaserScan-ranges", (object,), {
    "Line": 1181,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_LaserScan_ranges",
    "type": type("numBase-samples-LaserScan-ranges_type", (object,), {
        "Line": 1181, "CharPositionInLine": 37, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-LaserScan-remission"] = type("numBase-samples-LaserScan-remission", (object,), {
    "Line": 1185,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_LaserScan_remission",
    "type": type("numBase-samples-LaserScan-remission_type", (object,), {
        "Line": 1185, "CharPositionInLine": 40, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Pointcloud-points"] = type("numBase-samples-Pointcloud-points", (object,), {
    "Line": 1189,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Pointcloud_points",
    "type": type("numBase-samples-Pointcloud-points_type", (object,), {
        "Line": 1189, "CharPositionInLine": 38, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Pointcloud-colors"] = type("numBase-samples-Pointcloud-colors", (object,), {
    "Line": 1193,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Pointcloud_colors",
    "type": type("numBase-samples-Pointcloud-colors_type", (object,), {
        "Line": 1193, "CharPositionInLine": 38, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Sonar-timestamps"] = type("numBase-samples-Sonar-timestamps", (object,), {
    "Line": 1197,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Sonar_timestamps",
    "type": type("numBase-samples-Sonar-timestamps_type", (object,), {
        "Line": 1197, "CharPositionInLine": 37, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Sonar-bearings"] = type("numBase-samples-Sonar-bearings", (object,), {
    "Line": 1201,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Sonar_bearings",
    "type": type("numBase-samples-Sonar-bearings_type", (object,), {
        "Line": 1201, "CharPositionInLine": 35, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Sonar-bins"] = type("numBase-samples-Sonar-bins", (object,), {
    "Line": 1205,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Sonar_bins",
    "type": type("numBase-samples-Sonar-bins_type", (object,), {
        "Line": 1205, "CharPositionInLine": 31, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-SonarBeam-beam"] = type("numBase-samples-SonarBeam-beam", (object,), {
    "Line": 1209,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_SonarBeam_beam",
    "type": type("numBase-samples-SonarBeam-beam_type", (object,), {
        "Line": 1209, "CharPositionInLine": 35, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-SonarScan-data"] = type("numBase-samples-SonarScan-data", (object,), {
    "Line": 1213,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_SonarScan_data",
    "type": type("numBase-samples-SonarScan-data_type", (object,), {
        "Line": 1213, "CharPositionInLine": 35, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-SonarScan-time-beams"] = type("numBase-samples-SonarScan-time-beams", (object,), {
    "Line": 1217,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_SonarScan_time_beams",
    "type": type("numBase-samples-SonarScan-time-beams_type", (object,), {
        "Line": 1217, "CharPositionInLine": 41, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Wrenches-names"] = type("numBase-samples-Wrenches-names", (object,), {
    "Line": 1221,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Wrenches_names",
    "type": type("numBase-samples-Wrenches-names_type", (object,), {
        "Line": 1221, "CharPositionInLine": 35, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Wrenches-elements"] = type("numBase-samples-Wrenches-elements", (object,), {
    "Line": 1225,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Wrenches_elements",
    "type": type("numBase-samples-Wrenches-elements_type", (object,), {
        "Line": 1225, "CharPositionInLine": 38, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-JointTransformVector-names"] = type("numBase-JointTransformVector-names", (object,), {
    "Line": 1229,
    "CharPositionInLine": 4,
    "varName": "numBase_JointTransformVector_names",
    "type": type("numBase-JointTransformVector-names_type", (object,), {
        "Line": 1229, "CharPositionInLine": 39, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-JointTransformVector-elements"] = type("numBase-JointTransformVector-elements", (object,), {
    "Line": 1233,
    "CharPositionInLine": 4,
    "varName": "numBase_JointTransformVector_elements",
    "type": type("numBase-JointTransformVector-elements_type", (object,), {
        "Line": 1233, "CharPositionInLine": 42, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-Base-JointTransform-names"] = type("numBase-NamedVector-Base-JointTransform-names", (object,), {
    "Line": 1237,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_Base_JointTransform_names",
    "type": type("numBase-NamedVector-Base-JointTransform-names_type", (object,), {
        "Line": 1237, "CharPositionInLine": 50, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-Base-JointTransform-elements"] = type("numBase-NamedVector-Base-JointTransform-elements", (object,), {
    "Line": 1241,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_Base_JointTransform_elements",
    "type": type("numBase-NamedVector-Base-JointTransform-elements_type", (object,), {
        "Line": 1241, "CharPositionInLine": 53, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-frame-Frame-image"] = type("numBase-samples-frame-Frame-image", (object,), {
    "Line": 1245,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_frame_Frame_image",
    "type": type("numBase-samples-frame-Frame-image_type", (object,), {
        "Line": 1245, "CharPositionInLine": 38, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-frame-Frame-attributes"] = type("numBase-samples-frame-Frame-attributes", (object,), {
    "Line": 1249,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_frame_Frame_attributes",
    "type": type("numBase-samples-frame-Frame-attributes_type", (object,), {
        "Line": 1249, "CharPositionInLine": 43, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numWrappers-MatrixXd-data"] = type("numWrappers-MatrixXd-data", (object,), {
    "Line": 1253,
    "CharPositionInLine": 4,
    "varName": "numWrappers_MatrixXd_data",
    "type": type("numWrappers-MatrixXd-data_type", (object,), {
        "Line": 1253, "CharPositionInLine": 30, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numWrappers-VectorXd-data"] = type("numWrappers-VectorXd-data", (object,), {
    "Line": 1257,
    "CharPositionInLine": 4,
    "varName": "numWrappers_VectorXd_data",
    "type": type("numWrappers-VectorXd-data_type", (object,), {
        "Line": 1257, "CharPositionInLine": 30, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-JointTransformVector-m-names"] = type("numBase-JointTransformVector-m-names", (object,), {
    "Line": 1261,
    "CharPositionInLine": 4,
    "varName": "numBase_JointTransformVector_m_names",
    "type": type("numBase-JointTransformVector-m-names_type", (object,), {
        "Line": 1261, "CharPositionInLine": 41, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-base-JointTransform-m-names"] = type("numBase-NamedVector-base-JointTransform-m-names", (object,), {
    "Line": 1265,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_base_JointTransform_m_names",
    "type": type("numBase-NamedVector-base-JointTransform-m-names_type", (object,), {
        "Line": 1265, "CharPositionInLine": 52, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-NamedVector-base-Wrench-m-names"] = type("numBase-NamedVector-base-Wrench-m-names", (object,), {
    "Line": 1269,
    "CharPositionInLine": 4,
    "varName": "numBase_NamedVector_base_Wrench_m_names",
    "type": type("numBase-NamedVector-base-Wrench-m-names_type", (object,), {
        "Line": 1269, "CharPositionInLine": 44, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Pointcloud-m-points"] = type("numBase-samples-Pointcloud-m-points", (object,), {
    "Line": 1273,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Pointcloud_m_points",
    "type": type("numBase-samples-Pointcloud-m-points_type", (object,), {
        "Line": 1273, "CharPositionInLine": 40, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Pointcloud-m-colors"] = type("numBase-samples-Pointcloud-m-colors", (object,), {
    "Line": 1277,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Pointcloud_m_colors",
    "type": type("numBase-samples-Pointcloud-m-colors_type", (object,), {
        "Line": 1277, "CharPositionInLine": 40, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numBase-samples-Wrenches-m-names"] = type("numBase-samples-Wrenches-m-names", (object,), {
    "Line": 1281,
    "CharPositionInLine": 4,
    "varName": "numBase_samples_Wrenches_m_names",
    "type": type("numBase-samples-Wrenches-m-names_type", (object,), {
        "Line": 1281, "CharPositionInLine": 37, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numWrappers-geometry-Spline-knots"] = type("numWrappers-geometry-Spline-knots", (object,), {
    "Line": 1285,
    "CharPositionInLine": 4,
    "varName": "numWrappers_geometry_Spline_knots",
    "type": type("numWrappers-geometry-Spline-knots_type", (object,), {
        "Line": 1285, "CharPositionInLine": 38, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})

variables["numWrappers-geometry-Spline-vertices"] = type("numWrappers-geometry-Spline-vertices", (object,), {
    "Line": 1289,
    "CharPositionInLine": 4,
    "varName": "numWrappers_geometry_Spline_vertices",
    "type": type("numWrappers-geometry-Spline-vertices_type", (object,), {
        "Line": 1289, "CharPositionInLine": 41, "kind": "ReferenceType", "ReferencedTypeName": "T-UInt32", "Min": "0", "Max": "4294967295", "ReferencedModName": "TASTE-BasicTypes"
    }),
    "value": 200
})
