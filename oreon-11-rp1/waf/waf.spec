%global source0_hash e42a4cf7f7d57939a02490a1135a63845c4752eed35653b566132ddf2070bb7f

Name:           waf
Version:        2.1.9
Release:        2%{?dist}
Summary:        A Python-based build system
# The entire source code is BSD apart from pproc.py (taken from Python 2.5)
# Automatically converted from old format: BSD and Python - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND LicenseRef-Callaway-Python
URL:            https://waf.io/
# Original tarfile can be found at
# https://waf.io/waf-%%{version}.tar.bz2
# We remove waf logos, licensed CC BY-NC
Source:         waf-%{version}.stripped.tar.bz2
Source1:        unpack_wafdir.py
# also search for waflib in /usr/share/waf
Patch0:         waf-2.0.18-libdir.patch
# do not try to use the (removed) waf logos
Patch1:         waf-2.0.18-logo.patch
# do not add -W when running sphinx-build
Patch2:         waf-2.0.18-sphinx-no-W.patch

# Enable building without html docs (e.g. in case no recent sphinx is
# available)
%bcond_without docs

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with docs}
BuildRequires:  python3-sphinx
BuildRequires:  graphviz
BuildRequires:  ImageMagick
%endif # with docs

# waf-2.0.18-2 in F32 the first python3-only version (i.e. not having
# a -python3 subpackage). Do not hardcode that as Obsoletes: though,
# to be able to roll out e.g. a 2.0.19 for older Fedora branches, but
# maintain upgradability
Provides:       %{name}-python3 = %{version}-%{release}
Obsoletes:      %{name}-python3 < %{version}-%{release}

%if "%{?python3_version}" != ""
# Seems like automatic ABI dependency is not detected since the files
# are going to a non-standard location
Requires:       python(abi) = %{python3_version}
%endif

# the demo suite contains a perl module, which draws in unwanted
# provides and requires
%global __requires_exclude_from ^%{_docdir}/.*$
%global __provides_exclude_from ^%{_docdir}/.*$

%global _description %{expand:
Waf is a Python-based framework for configuring, compiling and
installing applications. It is a replacement for other tools such as
Autotools, Scons, CMake or Ant.}

%description %_description

%if %{with docs}
%package -n %{name}-doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description -n %{name}-doc %_description

This package contains the HTML documentation for %{name}.
%endif # with docs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
extras=
for f in waflib/extras/*.py ; do
  f=$(basename "$f" .py);
  if [ "$f" != "__init__" ]; then
    extras="${extras:+$extras,}$f" ;
  fi
done
%{__python3} ./waf-light --make-waf --strip --tools="$extras"

%if %{with docs}
# build html docs
export WAFDIR=$(pwd)
pushd docs/sphinx
%{__python3} ../../waf -v configure build
popd
%endif # with docs

%install
%{__python3} %{S:1} _temp
pushd _temp
find . -name '*.py' -printf '%%P\0' |
  xargs -0 -I{} install -m 0644 -p -D {} %{buildroot}%{_datadir}/waf3/{}
popd

# install the frontend
install -m 0755 -p -D waf-light %{buildroot}%{_bindir}/waf
ln -s waf %{buildroot}%{_bindir}/waf-3
ln -s waf %{buildroot}%{_bindir}/waf-%{python3_version}

# remove shebangs from and fix EOL for all scripts in wafadmin
find %{buildroot}%{_datadir}/ -name '*.py' \
     -exec sed -i -e '1{/^#!/d}' -e 's|\r$||g' {} \;

# fix waf script shebang line
sed -i "1c#! %{__python3}" %{buildroot}%{_bindir}/waf

# remove x-bits from everything going to doc
find demos utils -type f -exec chmod 0644 {} \;

# fix shebang lines in the demos
find demos \( -name '*.py' -o -name '*.py.in' -o -name 'wscript' -o -name 'wscript_build' \) \
  -exec sed -e '1{/^#!/d}' -e '1i#!%{__python3}' -i {} \;

# remove hidden file
rm -f docs/sphinx/build/html/.buildinfo

# do byte compilation
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/waf3

%files
%doc README.md ChangeLog demos
%{_bindir}/waf-%{python3_version}
%{_bindir}/waf-3
%{_bindir}/waf
%{_datadir}/waf3

%if %{with docs}
%files -n %{name}-doc
%doc docs/sphinx/build/html
%endif # with docs

%changelog
%autochangelog
