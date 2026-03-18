import GObject from 'gi://GObject';

export const LayoutManager = GObject.registerClass(
class LayoutManager extends GObject.Object {
    constructor() {
        super();
        this._startingUp = 1;
    }

    connectObject(object) {
    }

    disconnectObject(object) {
    }
});

export let layoutManager =  new LayoutManager();
