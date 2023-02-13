﻿using System;
using System.Collections.Generic;

namespace Helper
{
    /// <summary>
    /// Class that stores all the configuration information for the simulation
    /// </summary>
    public class Config
    {
        public CropConfig Prior = null;
        public CropConfig Current = null;
        public CropConfig Following = null;

        public List<CropConfig> Rotation = new List<CropConfig>();

        public FieldConfig Field = null;

        public Config(object[,] config)
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
