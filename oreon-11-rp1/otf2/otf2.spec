%global source0_hash 5a4e013a51ac4ed794fe35c55b700cd720346fda7f33ec84c76b86a5fb880a6e

# Note that we could package and use sionlib, which can improve otf2
# scalability, but it's not clear how worthwhile that might be for the
# packaging.  A maintainer says it will help around 8000 processes,
# and maybe fewer, and that building with it still allows reading and
# writing of non-sionlib traces.

Name:           otf2
Version:        3.1.1
Release:        6%{?dist}
Summary:        Open Trace Format 2 library

License:        BSD-3-Clause
URL:            http://score-p.org
Source0:        http://perftools.pages.jsc.fz-juelich.de/cicd/otf2/tags/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  chrpath dos2unix
# Need a new py-compile for Python 3.12
BuildRequires:  libtool automake
# "cannot determine instruction set" with these
ExcludeArch: i686 s390x

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
# CFLAGS etc. don't get passed to sub-configure unless given as args,
# and then configure fails for want of -fPIC.
%configure --disable-static --enable-shared --disable-silent-rules \
 --docdir=%{_pkgdocdir} --enable-backend-test-runs --with-platform=linux \
  CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS"
# With the binary extension, we should be installing into sitearch,
# not sitelib which otherwise gets used.  This is the easiest
# solution.  Fixme: patch to do the right thing.
sed -i -e '/"pythondir".*=/s;=.*$;="%{python3_sitearch}";' build-backend/config.status
# Avoid rpath in otf2-config
sed -i -e '/HARDCODE_INTO_LIBS/s/1/0/' build-backend/config.status
./config.status
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete
cp -p AUTHORS ChangeLog README %{buildroot}%{_pkgdocdir}/
chrpath -d %{buildroot}%{_bindir}/otf2-{marker,print,snapshots,estimator,config}
rm %{buildroot}%{_pkgdocdir}/python/.buildinfo

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/%{name}-estimator
%{_bindir}/%{name}-marker
%{_bindir}/%{name}-print
%{_bindir}/%{name}-snapshots
%{_libdir}/lib%{name}.so.10*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/%{name}.summary
%{_pkgdocdir}/AUTHORS
%{_pkgdocdir}/ChangeLog
%{_pkgdocdir}/OPEN_ISSUES
%{_pkgdocdir}/README
%exclude %{_pkgdocdir}/html
%exclude %{_pkgdocdir}/pdf
%exclude %{_pkgdocdir}/tags

%files devel
%{_bindir}/%{name}-config
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/otf2*.pc

%files doc
%license COPYING
%dir %{_pkgdocdir}
%{_pkgdocdir}/examples/
%{_pkgdocdir}/html/
%{_pkgdocdir}/pdf/
%{_pkgdocdir}/tags/
%{_pkgdocdir}/python/
%{_pkgdocdir}/CITATION.cff

%files -n python%{python3_pkgversion}-otf2
%{python3_sitearch}/%{name}/
%{python3_sitearch}/_%{name}/
%{_datadir}/%{name}/python

%changelog
%autochangelog
