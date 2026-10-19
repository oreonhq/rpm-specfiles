%global source0_hash 82b3a88a550cb8c3cec8fd45eca82cdcbaf945209977482471b4b5e430d64a8d
Name:           otf2
Version:        3.2
Release:        1%{?dist}
Summary:        Open Trace Format 2 library
License:        BSD-3-Clause
URL:            http://score-p.org
Source0:        http://perftools.pages.jsc.fz-juelich.de/cicd/otf2/tags/%{name}-%{version}/%{name}-%{version}.tar.gz
ExcludeArch: i686 s390x
# oreon:deps
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-six
# /oreon:deps
%description
The Open Trace Format 2 (OTF2) is a highly scalable, memory efficient
event trace data format plus support library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Development files for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation files for %{name}.

# Python packages can't be noarch as they require arch-specific otf2

%package -n python%{python3_pkgversion}-otf2
Summary:        Python 3 bindings for %{name}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-six
Requires:       python%{python3_pkgversion}-jinja2 python%{python3_pkgversion}-six
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n python%{python3_pkgversion}-otf2
Python 3 bindings for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
dos2unix doc/examples/otf2_high_level_writer_example.py
rm build-config/py-compile
for d in . build-backend build-frontend
do
  cd $d
  autoreconf -f -i -v
  cd -
done

%build

export PYTHON_FOR_GENERATOR=:
%configure --disable-static --enable-shared --disable-silent-rules \
 --docdir=%{_pkgdocdir} --enable-backend-test-runs --with-platform=linux \
  CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS"
sed -i -e '/"pythondir".*=/s;=.*$;="%{python3_sitearch}";' build-backend/config.status
sed -i -e '/HARDCODE_INTO_LIBS/s/1/0/' build-backend/config.status
./config.status
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -delete
cp -p AUTHORS ChangeLog README %{buildroot}%{_pkgdocdir}/
chrpath -d %{buildroot}%{_bindir}/otf2-{marker,print,snapshots,estimator,config}
rm %{buildroot}%{_pkgdocdir}/python/.buildinfo
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n otf2-devel -f %{oreon_filedir}/otf2-devel.list
%files -n otf2-doc -f %{oreon_filedir}/otf2-doc.list
%files -n python3-otf2 -f %{oreon_filedir}/python3-otf2.list

%changelog

%autochangelog
