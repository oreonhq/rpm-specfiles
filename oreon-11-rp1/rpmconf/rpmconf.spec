%global source0_hash 6f722a06a1c32d7f36542110e8b6818715e7864818ad2243326b0783d1b3a5c3

%bcond_with tests
%if 0%{?rhel} == 7
%global python3_pkgversion 36                                                                                                                           
%endif

Name:           rpmconf
Summary:        Tool to handle rpmnew and rpmsave files
License:        GPL-3.0-only
Version:        1.1.12
Release:        5%{?dist}
URL:            https://github.com/xsuchy/rpmconf
# source is created by:
# git clone https://github.com/xsuchy/rpmconf.git
# cd rpmconf; tito build --tgz
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  docbook-utils
BuildRequires:  docbook-dtd31-sgml
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       %{name}-base
Requires:       python%{python3_pkgversion}-rpmconf
Requires:       rpm-python3
BuildRequires:  rpm-python3
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pylint
BuildRequires:  python%{python3_pkgversion}-six
%endif
# mergetools
Suggests: diffuse
Suggests: diffutils
Suggests: kdiff3
Suggests: meld
Suggests: vim-X11
Suggests: vim-enhanced
# sdiff
Suggests: diffutils

%description
This tool search for .rpmnew, .rpmsave and .rpmorig files and ask you what to do
with them:
Keep current version, place back old version, watch the diff or merge.

%package -n python%{python3_pkgversion}-rpmconf
Summary:        Python interface for %{name}
BuildArch:      noarch

%description -n python%{python3_pkgversion}-rpmconf
Python interface for %{name}. Mostly useful for developers only.

%package -n python%{python3_pkgversion}-rpmconf-doc
Summary:        Documentation of python interface for %{name}
BuildArch:      noarch

%description -n python%{python3_pkgversion}-rpmconf-doc
Documentation generated from code of python3-rpmconf.

%package base
Summary: Filesystem for %{name}
BuildArch: noarch

%description base
Directory hierarchy for installation scripts, which are handled by rpmconf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
sed -i 's/__version__ = .*/__version__ = "%{version}"/' rpmconf/rpmconf.py
sed -i 's/version = .*,/version = "%{version}",/' setup.py 
%pyproject_wheel
docbook2man rpmconf.sgml
make -C docs html man

%install
%pyproject_install
#%{__python3} setup.py install --skip-build \
#    --install-scripts %{_sbindir} \
#    --root %{buildroot}
install -D -m 644 rpmconf.8 %{buildroot}%{_mandir}/man8/rpmconf.8
install -D -m 644 docs/build/man/rpmconf.3 %{buildroot}%{_mandir}/man3/rpmconf.3
mkdir -p %{buildroot}%{_datadir}/rpmconf/

%check
%if %{with tests}
pylint-3 rpmconf bin/rpmconf || :
%endif

%files
%license LICENSES/GPL-3.0-only.txt
%{_sbindir}/rpmconf
%{_mandir}/man8/rpmconf.8*
%doc README.md

%files -n python%{python3_pkgversion}-rpmconf
%license LICENSES/GPL-3.0-only.txt
%{python3_sitelib}/rpmconf/
%{python3_sitelib}/rpmconf-*.dist-info
%{_mandir}/man3/rpmconf.3*

%files -n python%{python3_pkgversion}-rpmconf-doc
%license LICENSES/GPL-3.0-only.txt
%doc docs/build/html/

%files base
%dir %{_datadir}/rpmconf

%changelog
%autochangelog
