﻿using System;
using System.Collections.Generic;

namespace Helper
{
    /// <summary>
    /// Class that stores all the configuration information for the simulation
    /// </summary>
    public static class Config2
    {
        public static CropConfig Prior = null;
        public static CropConfig Current = null;
        public static CropConfig Following = null;

        public static List<CropConfig> Rotation = new List<CropConfig>();

        public static FieldConfig Field = null;

        public static void Initialise(object[,] config)
        {
            Dictionary<string, object> c = Functions.dictMaker(config);
            Prior = new CropConfig(c, "Prior");
            Current = new CropConfig(c, "Current");
            Following = new CropConfig(c, "Following");
            Rotation = new List<CropConfig>() { Prior, Current, Following };
            Field = new FieldConfig(c);
        }
    }     
} 
