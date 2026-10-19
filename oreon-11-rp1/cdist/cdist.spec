%global source0_hash 78dbe687a63d54b4ea397b45b9fdc68b0df331fd8fa5c4aec685af265ca28546
%global __requires_exclude_from ^%{python3_sitelib}/%{name}/conf
%undefine __brp_mangle_shebangs
Name:		cdist
Version:	7.0.0
Release:        1%{?dist}
Summary:        Usable configuration management
License:	GPL-3.0-only
URL:		https://www.cdi.st/
Source0:        https://files.pythonhosted.org/packages/source/c/%{name}/%{name}-%{version}.tar.gz
Patch:	fix-argparse-scan.patch
BuildArch:	noarch
Requires:	bash
Requires:	openssh-clients
Recommends:	python3-scapy
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cdist = %{version}-%{release}
# /oreon:deps
%description
cdist is a usable configuration management system. It adheres to the KISS
principle and is being used in small up to enterprise grade environments. cdist
is an alternative to other configuration management systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{name}-%{version}

# Remove shebang on non-executable python files.
find . -type f -exec sed -i 's/^#!\/usr\/bin\/env python/#!\/usr\/bin\/python/' {} +

# Assume unverisoned python is python3.
find . -type f -exec sed -i 's/^#!\/usr\/bin\/python$/#!\/usr\/bin\/python3/' {} +

%build

%py3_build
%install
%py3_install
(cd %{buildroot}; grep -l -R -m 1 "^#!\/" . | xargs  chmod +x)
mkdir -p %{buildroot}%{_mandir}/man1/ %{buildroot}%{_mandir}/man7/
cp docs/dist/man/man1/*.1 %{buildroot}%{_mandir}/man1/
cp docs/dist/man/man7/*.7 %{buildroot}%{_mandir}/man7/
%oreon_autofiles cdist-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package doc
Summary: Documentation for the cdist configuration management tool
%description doc
HTML documentation for the cdist configuration management tool.

%files
%files -n cdist-doc -f %{oreon_filedir}/cdist-doc.list

%changelog

%autochangelog
