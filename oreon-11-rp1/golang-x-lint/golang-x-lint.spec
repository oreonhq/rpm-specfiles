%global source0_hash fdc1097539c7f8fbaa3796f8300614b586116c9a0c193c4955a70ff2cac97532
%bcond check 0
%global goipath         golang.org/x/lint
%global forgeurl        https://github.com/golang/lint
%global commit          83fdc39ff7b56453e3793356bcff3070b9b96445
%gometa
%global goaltipaths     github.com/golang/lint
%global common_description %{expand:
Golint is a linter for Go source code.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
%global vimfiles_root %{_datadir}/vim/vimfiles
Name:           %{goname}
Version:        0
Release:        1%{?dist}
Summary:        Linter for Go source code
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{commit}/lint-%{commit}.tar.gz
Obsoletes:      golint < 0-0.11
Provides:       golint = %{version}-%{release}
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(golang.org/x/tools/go/ast/astutil)
BuildRequires:  golang(golang.org/x/tools/go/gcexportdata)
# /oreon:deps
%description
%{common_description}

%package -n vim-golint
Requires:       %name
Requires:       vim-common
Summary: Golint vim plugin
%description -n vim-golint
%summary

# TODO package emacsXXXX package the emacs plug-in

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in golint; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{vimfiles_root}
cp -ar misc/vim/ftplugin %{buildroot}%{vimfiles_root}
%oreon_autofiles vim-golint usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n vim-golint -f %{oreon_filedir}/vim-golint.list

%changelog

%autochangelog
