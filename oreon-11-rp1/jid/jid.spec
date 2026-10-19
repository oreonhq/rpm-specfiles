%global source0_hash 0912050b3be3760804afaf7ecd6b42bfe79e7160066587fbc0afa5324b03fb48
%bcond check 0
%global goipath         github.com/simeji/jid
Version:                0.7.6
%gometa
%global goname          jid
%global common_description %{expand:
JSON Incremental Digger is a very simple JSON querying tool.
You can drill down JSON interactively by using filtering queries like jq.}
%global golicenses      LICENSE
%global godocs          ChangeLog README.md
Name:           %{goname}
Release:        23%{?dist}
Summary:        JSON incremental digger
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/bitly/go-simplejson)
BuildRequires:  golang(github.com/mattn/go-runewidth)
BuildRequires:  golang(github.com/nsf/termbox-go)
BuildRequires:  golang(github.com/nwidger/jsoncolor)
BuildRequires:  golang(github.com/pkg/errors)
BuildRequires:  golang(github.com/stretchr/testify/assert)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
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
