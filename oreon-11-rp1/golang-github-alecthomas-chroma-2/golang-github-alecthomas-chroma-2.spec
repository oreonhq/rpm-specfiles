%global source0_hash 45deb53e12a92cea43e797ed3d1edde0bf6ca7492d454126506e35e8822863a1
%bcond check 0
%global goipath         github.com/alecthomas/chroma/v2
Version:                2.27.0
%gometa -f
%global common_description %{expand:
A general purpose syntax highlighter in pure Go.}
%global golicenses      COPYING
%global godocs          pygments-lexers.txt README.md bin/README.hermit.md\\\
                        lexers/README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        A general purpose syntax highlighter in pure Go
License:        MIT
URL:            %{gourl}
Source0:        https://github.com/alecthomas/chroma/archive/v%{version}/chroma-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                     %{buildroot}%{_datarootdir}/gocode/src/github.com/alecthomas/chroma/v2/lexers/embedded
install -m 0644 -vp %{gobuilddir}/src/github.com/alecthomas/chroma/v2/lexers/embedded/* %{buildroot}%{_datarootdir}/gocode/src/github.com/alecthomas/chroma/v2/lexers/embedded
install -m 0755 -vd                     %{buildroot}%{_datarootdir}/gocode/src/github.com/alecthomas/chroma/v2/styles
install -m 0644 -vp %{gobuilddir}/src/github.com/alecthomas/chroma/v2/styles/* %{buildroot}%{_datarootdir}/gocode/src/github.com/alecthomas/chroma/v2/styles
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
