%global source0_hash 38aa5c60284f77cbb4be1de4af8907ce66954ff1a11e4f910d02e0283ce13b33
%bcond check 0
%global goipath         github.com/lunixbochs/vtclean
Version:                1.0.0
%gometa
%global common_description %{expand:
Clean up raw terminal output by stripping escape sequences, optionally
preserving color.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Strips terminal escapes from text, can preserve color
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/vtclean-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in vtclean; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
