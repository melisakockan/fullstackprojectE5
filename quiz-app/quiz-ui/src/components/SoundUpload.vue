<template>

    <div id="container_upload">
        <input
            tabindex="-1"
            type="file"
            name="uploadInput"
            :disabled="isSaving"
            @change="fileChange"
            accept=".mp3,.wav"
            class="input-file"
            ref="fileInput"
        />
        <a class="sound-upload-remove-link" 
                href="#" 
                v-if="file" 
                @click="clickRemoveSoundHandler">
                    Supprimer
        </a>
    </div>

</template>
<script>
export default {
  emits: ["file-change"],
  data() {
    return {
      isSaving: false,
      fileReader: null,
      fileInput: null,
      file: null
    };
  },
  props: {},
  mounted() {
    this.fileInput = this.$refs.fileInput;
    this.fileReader = new FileReader();
    this.fileReader.addEventListener(
      "load",
      () => {
        // fileReader holds a b64 string of the image
        const fileDataUrl = this.fileReader?.result;
        this.isSaving = false;
        this.$emit("file-change", fileDataUrl);
      },
      false
    );
  },
  methods: {
    fileChange(event) {
      this.isSaving = true;
      const input = event.target;
      // pick the first file uploaded
      this.file = input.files[0];
      // feed the file to the asynchronous file reader
      // (next step is in the load eventListener defined in mounted)
      this.fileReader.readAsDataURL(this.file);
    },
    clickRemoveSoundHandler() {
      this.file = null;
      this.$emit("file-change", "");
      if (this.fileInput) {
        this.fileInput.value = "";
      }
    }
  }
};
</script>

<style>
.sound-upload-remove-link {
  display: block;
}

#container_upload{
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    margin: 10px;
}




</style>