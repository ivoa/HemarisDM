package org.ivoa.dm.mymodel;
/*
 * Created on 10/05/2023 by Paul Harrison (paul.harrison@manchester.ac.uk).
 */

import org.ivoa.vodml.testing.AutoRoundTripWithValidationTest;

/**
 * This will run a XML and JSON round trip test on the model inst
 */
public class MymodelModelTest extends AutoRoundTripWithValidationTest<MymodelModel> {
    @Override
    public MymodelModel createModel() {
        // create the model instance here.
        MymodelModel retval = new MymodelModel();

        Another another = new Another("test");
        retval.addContent(another);
        return retval;
    }

    @Override
    public void testModel(MymodelModel mymodelModel) {
        //this could do specialized testing on the model instance
    }
}
