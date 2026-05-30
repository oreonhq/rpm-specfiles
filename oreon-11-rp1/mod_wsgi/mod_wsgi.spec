%global source0_hash 9a0fdb61405abc300ec6b100c440dd98cf31cb5f97aeef4207390937298cad20

%{!?_httpd_mmn: %{expand: %%global _httpd_mmn %%(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}}

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without python3
%bcond_with python2
%else
%bcond_with python3
%bcond_without python2
%endif

Name:           mod_wsgi
Version:        5.0.2
Release:        7%{?dist}
Summary:        A WSGI interface for Python web applications in Apache
License:        Apache-2.0 AND CC-BY-3.0
URL:            https://modwsgi.readthedocs.io/
Source0:        https://github.com/GrahamDumpleton/mod_wsgi/archive/%{version}.tar.gz#/mod_wsgi-%{version}.tar.gz
Source1:        wsgi.conf
Source2:        wsgi-python3.conf
Patch1:         mod_wsgi-4.5.20-exports.patch

BuildRequires:  httpd-devel
BuildRequires:  gcc
BuildRequires:  make

# Suppress auto-provides for module DSO
%global __provides_exclude_from %{_httpd_moddir}/.*\\.so$

%global _description\
The mod_wsgi adapter is an Apache module that provides a WSGI compliant\
interface for hosting Python based web applications within Apache. The\
adapter is written completely in C code against the Apache C runtime and\
for hosting WSGI applications within Apache has a lower overhead than using\
existing WSGI adapters for mod_python or CGI.\


%description %_description

%if %{with python2}
%package -n python2-%{name}
Summary: %summary
Requires:       httpd-mmn = %{_httpd_mmn}
BuildRequires:  python2-devel, python2-setuptools
%{?python_provide:%python_provide python2-%{name}}
%if 0%{?rhel} && 0%{?rhel} <= 7
Provides: mod_wsgi = %{version}-%{release}
Provides: mod_wsgi%{?_isa} = %{version}-%{release}
Obsoletes: mod_wsgi < %{version}-%{release}
%endif

%description -n python2-%{name} %_description

%endif

%if %{with python3}
%package -n python3-%{name}
Summary:        %summary
Requires:       httpd-mmn = %{_httpd_mmn}
BuildRequires:  python3-devel, python3-sphinx, python3-sphinx_rtd_theme
BuildRequires:  python3-setuptools
%if !%{with python2}
Provides: mod_wsgi = %{version}-%{release}
Provides: mod_wsgi%{?_isa} = %{version}-%{release}
Obsoletes: mod_wsgi < %{version}-%{release}
%endif

%description -n python3-%{name} %_description

%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{version}

: Python2=%{with python2} Python3=%{with python3}

%build
%if %{with python3}
%make_build -C docs html
%endif

export LDFLAGS="$RPM_LD_FLAGS -L%{_libdir}"
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"

%if %{with python3}
mkdir py3build/
# this always produces an error (because of trying to copy py3build
# into itself) but we don't mind, so || :
cp -R * py3build/ || :
pushd py3build
%configure --enable-shared --with-apxs=%{_httpd_apxs} --with-python=%{python3}
%make_build
%py3_build
popd
%endif

%if %{with python2}
%configure --enable-shared --with-apxs=%{_httpd_apxs} --with-python=%{python2}
%make_build
%py2_build
%endif

%install
# first install python3 variant and rename the so file
%if %{with python3}
pushd py3build
%make_install LIBEXECDIR=%{_httpd_moddir}
mv  $RPM_BUILD_ROOT%{_httpd_moddir}/mod_wsgi{,_python3}.so

install -d -m 755 $RPM_BUILD_ROOT%{_httpd_modconfdir}
# httpd >= 2.4.x
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-wsgi-python3.conf

%py3_install
mv $RPM_BUILD_ROOT%{_bindir}/mod_wsgi-express{,-3}
popd

%endif

# second install python2 variant
%if %{with python2}
%make_install LIBEXECDIR=%{_httpd_moddir}

install -d -m 755 $RPM_BUILD_ROOT%{_httpd_modconfdir}
# httpd >= 2.4.x
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_httpd_modconfdir}/10-wsgi.conf

%py2_install
mv $RPM_BUILD_ROOT%{_bindir}/mod_wsgi-express{,-2}
ln -s %{_bindir}/mod_wsgi-express-2 $RPM_BUILD_ROOT%{_bindir}/mod_wsgi-express
%endif

%if %{with python2}
%files -n python2-%{name}
%license LICENSE
%doc CREDITS.rst README.rst
%config(noreplace) %{_httpd_modconfdir}/*wsgi.conf
%{_httpd_moddir}/mod_wsgi.so
%{python2_sitearch}/mod_wsgi-*.egg-info
%{python2_sitearch}/mod_wsgi
%{_bindir}/mod_wsgi-express-2
%{_bindir}/mod_wsgi-express
%endif

%if %{with python3}
%files -n python3-%{name}
%license LICENSE
%doc CREDITS.rst README.rst
%config(noreplace) %{_httpd_modconfdir}/*wsgi-python3.conf
%{_httpd_moddir}/mod_wsgi_python3.so
%{python3_sitearch}/mod_wsgi-*.egg-info
%{python3_sitearch}/mod_wsgi
%{_bindir}/mod_wsgi-express-3
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.2-7
- Prepare for Oreon 11 (RP1)
