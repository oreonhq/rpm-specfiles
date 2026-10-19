%global source0_hash 0c9d79b4e8149dd120584809709d79b628ded4f4d63603fb132d5a055a513573
%bcond check 0
%global goipath         github.com/gosexy/gettext
Version:                0.9
%gometa
%global godevelheader %{expand:
Requires:       gettext-devel}
%global common_description %{expand:
Go bindings for GNU gettext, an internationalization and localization library
for writing multilingual systems.}
%global golicenses      LICENSE
%global godocs          _examples README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go bindings for GNU's gettext
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/gettext-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  gettext-devel
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/jessevdk/go-flags)
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(gopkg.in/check.v1)
# /oreon:deps
%description
%{common_description}

%package -n go-xgettext
Summary:        Program for extracting translatable strings from Go programs
%description -n go-xgettext
The go-xgettext program is an implementation of xgettext implemented in go.
It can reliably parse go source files to identify content to translate.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in go-xgettext; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles go-xgettext usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck -d .
%endif
%files -f %{oreon_filedir}/main.list
%files -n go-xgettext -f %{oreon_filedir}/go-xgettext.list

%changelog

%autochangelog
