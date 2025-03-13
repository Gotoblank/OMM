use omm;

INSERT INTO tag(dtype, tag_name) VALUES("Category", "autonomics");
INSERT INTO tag(dtype, tag_name) VALUES("Category", "anatomy");
INSERT INTO tag(dtype, tag_name) VALUES("Category", "biomechanics");
INSERT INTO tag(dtype, tag_name) VALUES("Category", "lymphatics");
INSERT INTO tag(dtype, tag_name) VALUES("Category", "heent");
INSERT INTO tag(dtype, tag_name) VALUES("Category", "cardiopulmonary");
INSERT INTO tag(dtype, tag_name) VALUES("Category", "gastrointestinal");
INSERT INTO tag(dtype, tag_name) VALUES("Category", "pregnancy");
INSERT INTO tag(dtype, tag_name) VALUES("Category", "pediatrics");
INSERT INTO tag(dtype, tag_name) VALUES("Category", "orthopedic/gaint");

INSERT INTO tag(dtype, tag_name) VALUES("Body region", "head");
INSERT INTO tag(dtype, tag_name) VALUES("Body region", "cervical");
INSERT INTO tag(dtype, tag_name) VALUES("Body region", "thoracic");
INSERT INTO tag(dtype, tag_name) VALUES("Body region", "lumbar");
INSERT INTO tag(dtype, tag_name) VALUES("Body region", "pelvis");
INSERT INTO tag(dtype, tag_name) VALUES("Body region", "sacrum");
INSERT INTO tag(dtype, tag_name) VALUES("Body region", "lower extremity");
INSERT INTO tag(dtype, tag_name) VALUES("Body region", "upper extremity");
INSERT INTO tag(dtype, tag_name) VALUES("Body region", "ribs");
INSERT INTO tag(dtype, tag_name) VALUES("Body region", "abdomen");


INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "mysofacial release (MFR)/soft tissue (ST)");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "muscle energy (ME)");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "high-velocity low-amplitude (HVLA)");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "counterstrain (CS)");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "facilitated positional release (FPR)");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "balanced ligamentous tension (BLT)");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "still technique");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "cranial rechniques");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "lymphatics techniques");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "mechanism of action (MOA)");
INSERT INTO tag(dtype, tag_name) VALUES("Treatment Techniques", "indications/contraindication to treatment");

select * from tag;