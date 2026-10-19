%global source0_hash 769f261a2eb031ce924f172dc91fa9889ed5a2a01f93a12b863192e31f93be65
%bcond check 0
%global goipath         github.com/tinylib/msgp
Version:                1.1.5
%gometa
%global common_description %{expand:
This is a code generation tool and serialization library for MessagePack.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go code generator for MessagePack
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/msgp-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
# /oreon:deps
%package -n       msgp
Summary:        Go code generator for MessagePack
BuildArch:      noarch

%description -n msgp
Go code generator for MessagePack

%description
%{common_description}

%package -n msgp
Summary:        Go code generator for MessagePack
%description -n msgp
%{common_description}

This package contains the msgp binary.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/msgp %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles msgp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

export GO111MODULE=off
export PATH=$PATH:%{buildroot}%{_bindir}
export GOPATH=%{_datadir}/gocode:%{buildroot}%{_datadir}/gocode
go generate ./msgp
go generate ./_generated
%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n msgp -f %{oreon_filedir}/msgp.list

%changelog

%autochangelog
