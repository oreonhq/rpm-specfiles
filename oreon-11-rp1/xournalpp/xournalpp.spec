%global source0_hash none
%bcond cppunit  1
%bcond gtest 1
%bcond profiling 1
%bcond qpdf 1
%global forgeurl https://github.com/xournalpp/xournalpp
Name:           xournalpp
Version:        1.3.7
Release:        1%{?dist}
Summary:        Handwriting note-taking software with PDF annotation support
License:        GPL-2.0-or-later
%forgemeta
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
%if %{with cppunit}
%endif
%if %{with gtest}
%endif
%if %{with profiling}
%endif
%if %{with qpdf}
%endif
Recommends:     texlive-latex-bin
Requires:       hicolor-icon-theme
Requires:       %{name}-plugins = %{version}-%{release}
Requires:       %{name}-ui = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  help2man
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libprofiler)
BuildRequires:  pkgconfig(libqpdf)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(sndfile)
# /oreon:deps
%description
Xournal++ is a handwriting note-taking application with PDF annotation support.
It is optimized for pen input such as Wacom tablets.

%package plugins
Summary:        Default plugins for %{name}
BuildArch:      noarch
%description plugins
This package contains sample plugins for %{name}.

%package ui
Summary:        User interface files for %{name}
BuildArch:      noarch
%description ui
This package contains user interface resources for %{name}.

%prep

%forgeautosetup -p1

%build

%cmake \
    -DCMAKE_BUILD_TYPE="Release" \
    -DDISTRO_CODENAME="Fedora Linux" \
    -DENABLE_GTEST=%{with gtest} \
    -DENABLE_PROFILING=%{with profiling}
%cmake_build
%install
%cmake_install
%find_lang %{name}
install -d '%{buildroot}%{_mandir}/man1'
for cmd in %{buildroot}%{_bindir}/*
do
  LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
      help2man \
      --no-info --no-discard-stderr --version-string='%{version}' \
      --output="%{buildroot}%{_mandir}/man1/$(basename "${cmd}").1" \
      "${cmd}"
done
find %{buildroot} -name "*.sh" -delete
%fdupes %{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/com.github.%{name}.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/com.github.%{name}.%{name}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n xournalpp-plugins -f %{oreon_filedir}/xournalpp-plugins.list
%files -n xournalpp-ui -f %{oreon_filedir}/xournalpp-ui.list

%changelog

%autochangelog
