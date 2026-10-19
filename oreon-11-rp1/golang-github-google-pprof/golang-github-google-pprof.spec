%global source0_hash f1bbd9fcc9768444dc024d2ef9bcd0037ca19148c5a46cdcc426e656d175a284
%bcond check 0
%global goipath         github.com/google/pprof
%global commit          c50bf4fe530358fa651598413f786f4367e26268
%gometa
%global common_description %{expand:
Pprof is a tool for visualization and analysis of profiling data.
Pprof reads a collection of profiling samples in profile.proto format and
generates reports to visualize and help analyze the data. It can generate both
text and graphical reports (through the use of the dot visualization package).}
%global golicenses      LICENSE LICENSE-*
%global godocs          doc AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Tool for visualization and analysis of profiling data
License:        LicenseRef-Callaway-BSD AND Apache-2.0
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/pprof-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
mv third_party/d3/LICENSE LICENSE-d3
mv third_party/d3flamegraph/LICENSE LICENSE-d3flamegraph
mv third_party/svgpan/LICENSE LICENSE-svgpan

%build

%gobuild -o %{gobuilddir}/bin/pprof %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck -d internal/binutils -d internal/report
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
