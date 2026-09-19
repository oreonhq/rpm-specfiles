%global source0_hash dbf3be9c8123429c8a73ebd4c18993331619198e88fa40dde99f48213fa75012

Name:           python3-poppler-qt5
Version:        21.3.0
Release:        15%{?dist}
Summary:        Python bindings for the Poppler PDF rendering library

License:        LGPL-2.1-or-later
URL:            https://github.com/frescobaldi/python-poppler-qt5
Source0:        %{url}/archive/v%{version}.tar.gz#/python-poppler-qt5-%{version}.tar.gz
Patch0:         binpaths.patch
Patch1:         40e71ad88173d02648bceb2438bc0567e60dacd5.patch
Requires: python3-qt5
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-qt5-devel
BuildRequires:  %{py3_dist sip} >= 5
BuildRequires:  %{py3_dist PyQt-builder}
BuildRequires:  pkgconfig(poppler-qt5)

# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

%description
Python 3 bindings for the Poppler PDF rendering library. It is needed to
run programs written in Python 3 and using Poppler set.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn python-poppler-qt5-%{version}

%patch -P0 -p0
#%patch1 -p1

%build
sip-build --qmake=%{_qt5_qmake} --verbose --no-make \
  --qmake-setting 'QMAKE_CFLAGS_RELEASE="%{optflags}"' \
  --qmake-setting 'QMAKE_CXXFLAGS_RELEASE="%{optflags}"' \
  --qmake-setting 'QMAKE_LFLAGS_RELEASE="%{?__global_ldflags}"'
%make_build -C build

%install
%make_install INSTALL_ROOT=%{buildroot} -C build
chmod +x %{buildroot}/%{python3_sitearch}/*.so

%files
%license LICENSE
%doc README.rst
%{python3_sitearch}/popplerqt5.cpython-*.so
%{python3_sitearch}/python_poppler*
%{python3_sitearch}/PyQt5/bindings/popplerqt5

%changelog
%autochangelog
