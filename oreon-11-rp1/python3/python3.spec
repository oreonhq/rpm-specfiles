%global source0_hash ba4bed1ba346b916890b76d9e320451420aa69f6408997d33c66482eeae3d575
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}
%global __brp_python_bytecompile %{nil}

Name: python3
Version: 3.15.0
Release: 4%{?dist}
Provides: python(abi) = 3.15
Summary: an interpreted, interactive, object-oriented programming language
License: Python-2.0.1
URL: https://www.python.org/
Source0: https://www.python.org/ftp/python/%{version}/Python-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: zlib-devel
BuildRequires: xz-devel
BuildRequires: bzip2-devel
BuildRequires: libffi-devel
BuildRequires: pkgconf
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
python - an interpreted, interactive, object-oriented programming language

%package devel
Summary: an interpreted, interactive, object-oriented programming language
Requires: python3%{?_isa} = %{version}-%{release}
Provides: pkgconfig(python3)
Provides: pkgconfig(python-3.15)

%description devel
python - an interpreted, interactive, object-oriented programming language

%prep
%oreon_sha256
%autosetup -n Python-%{version} -p1

%build
%oreon_configure --enable-shared --without-ensurepip --with-openssl=/no-such-openssl
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.a
ln -sf python3 %{buildroot}%{_bindir}/python
find %{buildroot} -type f -exec grep -I -l -E '^#! */usr/bin/env python$' {} + | while read f; do
  sed -i '1s|^#! */usr/bin/env python$|#!/usr/bin/python3|' "$f"
done
export PYTHONHASHSEED=0
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
find %{buildroot}/usr/lib %{buildroot}%{_libdir} -maxdepth 1 -type d -name 'python3.*' | while read d; do
  %{buildroot}%{_bindir}/python3.15 -B -m compileall -q -f -o 0 -o 1 -s %{buildroot} -p / --invalidation-mode=timestamp -x 'bad_coding|badsyntax|lib2to3/tests/data' "$d"
done

%oreon_filelist_devel
while read -r f; do
  case "$f" in
    */lib-dynload/*|*/idlelib/config-*) printf '%s\n' "$f" >> %{_builddir}/%{name}.files ;;
    *) printf '%s\n' "$f" >> %{_builddir}/%{name}-devel.files.new ;;
  esac
done < %{_builddir}/%{name}-devel.files
mv %{_builddir}/%{name}-devel.files.new %{_builddir}/%{name}-devel.files

%files -f %{_builddir}/%{name}.files
%license LICENSE

%files devel -f %{_builddir}/%{name}-devel.files

%changelog
* Mon Oct 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.15.0-1
- 3.15.0
