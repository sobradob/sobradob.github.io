# {{ .Title }}

{{ with .Description }}> {{ . }}{{ end }}

{{ with .Date }}**Date:** {{ .Format "2006-01-02" }}{{ end }}
{{ with .Params.categories }}**Categories:** {{ delimit . ", " }}{{ end }}
{{ with .Params.tags }}**Tags:** {{ delimit . ", " }}{{ end }}

---

{{ .RawContent }}
