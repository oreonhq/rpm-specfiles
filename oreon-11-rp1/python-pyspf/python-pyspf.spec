%global source0_hash 57a7ef01bda090173aafb6af0106251686ed73f03db4e911fcd34c57fc347186

%global srcname pyspf

Name:           python-%{srcname}
Version:        2.0.14
Release:        30%{?dist}
Summary:        Python module and programs for SPF (Sender Policy Framework)

# Automatically converted from old format: Python - review is highly recommended.
License:        LicenseRef-Callaway-Python
URL:            http://pypi.python.org/pypi/pyspf
# Also see http://bmsi.com/python/milter.html
Source0:        https://files.pythonhosted.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         pyspf-2.0.14-newlines.patch

BuildArch:      noarch

%description
SPF does email sender validation.  For more information about SPF,
please see http://spf.pobox.com.

This SPF client is intended to be installed on the border MTA, checking
if incoming SMTP clients are permitted to forward mail.  The SPF check
should be done during the MAIL FROM:<...> command.

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# For tests
# BuildRequires:  python2-yaml
# Not yet packaged
# BuildRequires:  python-authres

Requires:       python3-py3dns
%{?python_provide:%python_provide python3-%{srcname}}

Requires(post):   alternatives
Requires(postun): alternatives

%description -n python3-%{srcname}
SPF does email sender validation.  For more information about SPF,
please see http://spf.pobox.com.

This SPF client is intended to be installed on the border MTA, checking
if incoming SMTP clients are permitted to forward mail.  The SPF check
should be done during the MAIL FROM:<...> command.

This package provides Python 3 build of %{srcname}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{srcname}-%{version}
%patch -P0 -p1 -b .newlines

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%check
# Tests require unpackaged python-authres

%post -n python3-%{srcname}
[[ -f %{_bindir}/spfquery && \
   $(sha256sum %{_bindir}/spfquery{,.%{name}} | sort -k 1,1 -u | wc -l) = 1 ]] \
&& rm -f %{_bindir}/spfquery
update-alternatives --install %{_bindir}/spfquery spf %{_bindir}/spfquery.%{name} 10

%postun -n python3-%{srcname}
if [ $1 -eq 0 ] ; then
  update-alternatives --remove spf %{_bindir}/spfquery.%{name}
fi

%install
%pyproject_install
mv %{buildroot}%{_bindir}/type99.py %{buildroot}%{_bindir}/type99
mv %{buildroot}%{_bindir}/spfquery.py %{buildroot}%{_bindir}/spfquery.%{name}
rm -f %{buildroot}%{_bindir}/*.py{o,c}
# Remove shebang from python libraries
sed -i -e '/^#!\//, 1d' %{buildroot}%{python3_sitelib}/*.py

%files -n python3-%{srcname}
%doc CHANGELOG PKG-INFO README.md
%{python3_sitelib}/__pycache__
%{_bindir}/type99
%{_bindir}/spfquery.%{name}
%ghost %{_bindir}/spfquery
%{python3_sitelib}/spf.py*
%{python3_sitelib}/pyspf-%{version}.dist-info

%changelog
%autochangelog
