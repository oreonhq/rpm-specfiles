%global source0_hash 40c6d1e72eaaa200ccc1491ee4e4366fef7766c1604397725a8a3a6025c38ae8

Name:           simspark
Version:        0.3.5
Release:        14%{?dist}
Summary:        Spark physical simulation system

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://simspark.sourceforge.net
Source0:        http://downloads.sourceforge.net/simspark/%{name}-%{version}.tar.xz
Patch0:         %{name}-confscript-mlibfix.patch
# https://gitlab.com/robocup-sim/SimSpark/-/merge_requests/53
Patch1:         %{name}-pr53-cxx-header-include.patch
# Fix compilation with gcc15
# https://gitlab.com/robocup-sim/SimSpark/-/merge_requests/74
Patch2:         %{name}-pr74-gcc15-resolve-ambiguous-override.patch

BuildRequires: make
BuildRequires:  gcc gcc-c++ cmake boost-devel ruby ruby-devel SDL-devel tex(latex)
BuildRequires:  ode-devel libGL-devel DevIL-devel freetype-devel libGLU-devel
BuildRequires:  ImageMagick tex(titlesec.sty) tex(wrapfig.sty)
BuildRequires:  tex(subfigure.sty) qt5-qtbase-devel git
Conflicts:      rcssserver3d < 0.6.1
Requires:       ruby ruby(release)
Requires:       dejavu-sans-mono-fonts

%description
Spark is a physical simulation system. The primary purpose of this system is
to provide a *generic* simulator for different kinds of simulations.
In these simulations, agents can participate as external processes. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa} ruby-devel%{?_isa} ode-devel%{?_isa}
Requires:       DevIL-devel%{?_isa} libGL-devel libGLU-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git

%build
mkdir build
cd build
export CXXFLAGS="${CXXFLAGS:-%optflags} -std=gnu++98"
export CFLAGS="${CFLAGS:-%optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIBDIR:PATH=%{_lib} -DODE_CONFIG_EXEC=ode-double-config .. \
  -DRUBY_INCLUDE_PATH=`ruby -e 'puts File.join(RbConfig::CONFIG[%q(includedir)], RbConfig::CONFIG[%q(sitearch)])'`
make VERBOSE=1 %{?_smp_mflags}
make pdf
cp doc/devel/manual.pdf ../doc/devel/

%install
make -C build install DESTDIR=%{buildroot}

ln -fs %{_datadir}/fonts/dejavu/DejaVuSansMono.ttf \
      %{buildroot}/%{_datadir}/%{name}/fonts/VeraMono.ttf
rm -rf %{buildroot}/%{_datadir}/%{name}/*.h

mkdir package_docs
mv %{buildroot}/%{_datadir}/doc/%{name}/* package_docs/
rm -rf %{buildroot}/%{_datadir}/doc

%files
%doc package_docs/*
%dir %{_libdir}/%{name}
# Notice: the package needs .so files for running so
# they can't be moved to -devel package
%{_libdir}/%{name}/[^l]*.so*
%{_libdir}/%{name}/lib*.so.*
%{_libdir}/gui*/*.so
%{_datadir}/%{name}
%{_datadir}/carbon

%files devel
%{_bindir}/*
%{_includedir}/%{name}
%{_includedir}/gui*
%{_libdir}/%{name}/lib*.so
%doc doc/devel/manual.pdf

%changelog
%autochangelog
