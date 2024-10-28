{{/*
Generate the chart name.
*/}}
{{- define "flexmaster-chart.name" -}}
{{ .Chart.Name }}
{{- end }}

{{/*
Generate the full name for resources.
*/}}
{{- define "flexmaster-chart.fullname" -}}
{{ printf "%s-%s" .Release.Name (include "flexmaster-chart.name" .) | trunc 63 | trimSuffix "-" }}
{{- end }}
