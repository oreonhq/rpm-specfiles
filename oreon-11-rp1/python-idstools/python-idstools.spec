%global source0_hash a0ecc4f7887e3d22a1a98e1c88108d37a523adf8a3756ee557d60860c2c563b7

# Warning:
# Anyone editing this spec file please make sure the same spec file
# works on other fedora and epel releases, which are supported by this software.
# No quick Rawhide-only fixes will be allowed.

%global		upstream_name	py-idstools
%global		pname		idstools

Name:		python-%{pname}
Version:	0.6.5
Release:	13%{?dist}
Summary:	Snort and Suricata Rule and Event Utilities
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/jasonish/py-idstools
Source0:	https://github.com/jasonish/py-idstools/archive/%{version}.tar.gz#/%{upstream_name}-%{version}.tar.gz
BuildArch:	noarch

%global desc_base \
	py-idstools is a collection of Python libraries for working with IDS systems\
	(typically Snort and Suricata).

%description
%{desc_base}

%package -n python%{python3_pkgversion}-%{pname}
Summary:	%{summary} for Python3
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pname}}
Conflicts:	python2-%{pname} < 0.6.3-7

BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-pytest

Requires:	python%{python3_pkgversion}-dateutil

%description -n python%{python3_pkgversion}-%{pname}
%{desc_base} For Python3.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream_name}-%{version}
pushd tests
popd
# remove bundled libraries
%{__rm} -rf idstools/compat
%{__sed} -i '/compat/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python%{python3_pkgversion}-%{pname}
%{_bindir}/%{pname}-dumpdynamicrules
%{_bindir}/%{pname}-eve2pcap
%{_bindir}/%{pname}-gensidmsgmap
%{_bindir}/%{pname}-rulecat
%{_bindir}/%{pname}-rulemod
%{_bindir}/%{pname}-u2eve
%{_bindir}/%{pname}-u2fast
%{_bindir}/%{pname}-u2json
%{_bindir}/%{pname}-u2spewfoo
%{python3_sitelib}/%{pname}-%{version}.dist-info
%{python3_sitelib}/%{pname}
%doc README.rst

%changelog
%autochangelog
