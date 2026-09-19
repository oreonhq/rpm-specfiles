%global source0_hash none

#global svndate 20250315
#global svnrev 13634
%global snapshot 0%{?svndate}
%if %{snapshot}
%global svnrelease .%{svndate}svn%{svnrev}
%endif

Name:		codeblocks
Version:	25.03
Release:	5%{?svnrelease}%{?dist}
Summary:	An open source, cross platform, free C++ IDE
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://www.codeblocks.org/
%if %{snapshot}
# fedora-getsvn codeblocks svn://svn.code.sf.net/p/codeblocks/code/trunk %%{svnrev}
Source0:	%{name}-svn%{svnrev}.tar.bz2
%else
Source0:	https://sourceforge.net/projects/%{name}/files/Sources/%{version}/%{name}_%{version}.tar.xz
%endif
Patch0:		codeblocks-autorev.patch
# use distro compiler standards
Patch1:		codeblocks-flags.patch
# backported fixes
Patch2:		codeblocks-fedora.patch

BuildRequires:	astyle-devel >= 3.1
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	desktop-file-utils
BuildRequires:	dos2unix
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	hunspell-devel
BuildRequires:	libappstream-glib
BuildRequires:	libICE-devel
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	tinyxml-devel
BuildRequires:	wxGTK-devel
BuildRequires:	zip
BuildRequires:	zlib-devel
%if 0%{?rhel} && 0%{?rhel} <= 9
BuildRequires:	autoconf2.7x
%endif

Requires:	%{name}-libs = %{version}-%{release}
Requires:	shared-mime-info
Requires:	xterm
Recommends:	%{name}-contrib
Provides:	bundled(wxScintilla) = 3.53.0
# patched with https://github.com/albertodemichelis/squirrel/issues/230 (svn rev 12365)
Provides:	bundled(squirrel) = 3.1

%global		pkgdatadir	%{_datadir}/%{name}
%global		pkglibdir	%{_libdir}/%{name}
%global		plugindir	%{pkglibdir}/plugins

%global __provides_exclude_from ^%{plugindir}/.*\\.so$

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
Code::Blocks is a free C++ IDE built specifically to meet the most demanding
needs of its users. It was designed, right from the start, to be extensible
and configurable. Built around a plug-in framework, Code::Blocks can be
extended with plug-in DLLs. It includes a plugin wizard, so you can compile
your own plug-ins.

%package libs
Summary:	Libraries needed to run Code::Blocks and its plug-ins

%description libs
Libraries needed to run Code::Blocks and its plug-ins.

%package devel
Summary:	Files needed to build Code::Blocks plug-ins
Requires:	%{name}-libs = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development files needed to build Code::Blocks plug-ins.

%package contrib-libs
Summary:	Libraries needed to run Code::Blocks contrib plug-ins
Requires:	%{name}-libs = %{version}-%{release}

%description contrib-libs
Libraries needed to run Code::Blocks contrib plug-ins.

%package contrib-devel
Summary:	Files needed to build Code::Blocks contrib plug-ins
Requires:	%{name}-contrib-libs = %{version}-%{release}

%description contrib-devel
Development files needed to build Code::Blocks contrib plug-ins.

%package contrib
Summary:	Additional Code::Blocks plug-ins
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-contrib-libs = %{version}-%{release}
Recommends:	cppcheck
Recommends:	cscope
Recommends:	valgrind

%description contrib
Additional Code::Blocks plug-ins.

%prep
%if %{snapshot}
%setup -q -n %{name}
%patch -P 0 -p1
%else
%setup -q -n %{name}_%{version}
%endif
%patch -P 1 -p1
%patch -P 2 -p1

%if %{snapshot}
# generate revision.m4
echo "m4_define([SVN_REV], %{svnrev})" > revision.m4
echo "m4_define([SVN_REVISION], svn%{svnrev})" >> revision.m4
echo "m4_define([SVN_DATE], %{svndate})" >> revision.m4

./bootstrap
%else
%if 0%{?rhel} && 0%{?rhel} <= 9
autoreconf27 -f -i
%else
autoreconf -f -i
%endif
%endif

# convert EOLs
find . -type f -and -not -name "*.cpp" -and -not -name "*.h" -and -not -name "*.png" -and -not -name "*.bmp" -and -not -name "*.c" -and -not -name "*.cxx" -and -not -name "*.ico" -exec dos2unix -q --keepdate {} \;

%build

%configure \
    --with-contrib-plugins="all" \
    --with-boost-libdir=%{_libdir}

# remove unbundled stuff
rm -rf src/include/tinyxml src/base/tinyxml
rm -rf src/plugins/astyle/astyle
rm -rf src/plugins/contrib/SpellChecker/hunspell
rm -rf src/plugins/contrib/devpak_plugin/bzip2
rm -rf src/plugins/contrib/help_plugin/{bzip2,zlib}

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.{appdata,metainfo}.xml
desktop-file-validate	%{buildroot}/%{_datadir}/applications/codeblocks.desktop

find %{buildroot} -type f -name "*.la" -delete

# set a fixed timestamp (source archive creation) to generated resource archives
/bin/touch -r %{SOURCE0} %{buildroot}/%{pkgdatadir}/*.zip

# generate linker config file for wxContribItems libraries
mkdir -p %{buildroot}/%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/%{name}/wxContribItems" > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}-contrib-%{_arch}.conf

%ldconfig_scriptlets libs

%ldconfig_scriptlets contrib-libs

rm -f %{buildroot}/%{pkgdatadir}/docs/index.ini

%files
%license COPYING
%doc README AUTHORS BUGS COMPILERS NEWS
%{_bindir}/codeblocks
%{_bindir}/cb_*
%{_mandir}/man1/codeblocks.*.gz
%{_mandir}/man1/cb_console_runner.*.gz
%{_mandir}/man1/cb_share_config.*.gz

%dir %{pkglibdir}
%dir %{plugindir}
%{plugindir}/libAstyle.so
%{plugindir}/libabbreviations.so
%{plugindir}/libautosave.so
%{plugindir}/libclasswizard.so
%{plugindir}/libcodecompletion.so
%{plugindir}/libcompiler.so
%{plugindir}/libdebugger.so
%{plugindir}/libdefaultmimehandler.so
%{plugindir}/liboccurrenceshighlighting.so
%{plugindir}/libopenfileslist.so
%{plugindir}/libprojectsimporter.so
%{plugindir}/libscriptedwizard.so
%{plugindir}/libtodo.so

%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/mimetypes/*.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png

%dir %{pkgdatadir}
%{pkgdatadir}/icons
%dir %{pkgdatadir}/images
%{pkgdatadir}/images/*.png
%{pkgdatadir}/images/settings
%{pkgdatadir}/lexers
%{pkgdatadir}/scripts
%{pkgdatadir}/templates
%{pkgdatadir}/Astyle.zip
%{pkgdatadir}/abbreviations.zip
%{pkgdatadir}/autosave.zip
%{pkgdatadir}/classwizard.zip
%{pkgdatadir}/codecompletion.zip
%{pkgdatadir}/compiler.zip
%{pkgdatadir}/debugger.zip
%{pkgdatadir}/defaultmimehandler.zip
%{pkgdatadir}/manager_resources.zip
%{pkgdatadir}/occurrenceshighlighting.zip
%{pkgdatadir}/openfileslist.zip
%{pkgdatadir}/projectsimporter.zip
%{pkgdatadir}/resources.zip
%{pkgdatadir}/scriptedwizard.zip
%{pkgdatadir}/start_here.zip
%{pkgdatadir}/todo.zip
%{pkgdatadir}/tips.txt
%dir %{pkgdatadir}/compilers
%{pkgdatadir}/compilers/*.xml

%files libs
%doc COPYING
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%exclude %{_includedir}/%{name}/wxContribItems/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files contrib-libs
%{_sysconfdir}/ld.so.conf.d/%{name}-contrib-%{_arch}.conf
%{_libdir}/libwxsmithlib.so.*
%{_libdir}/%{name}/wxContribItems/*.so.*
%exclude %{_libdir}/libwxsmithlib.so

%files contrib-devel
%{_includedir}/wxsmith
%{_includedir}/%{name}/wxContribItems/
%{_libdir}/%{name}/wxContribItems/*.so
%{_libdir}/pkgconfig/cb_wx*.pc
%{_libdir}/pkgconfig/wxsmith.pc
%{_libdir}/pkgconfig/wxsmithaui.pc
%{_libdir}/pkgconfig/wxsmith-contrib.pc

%files contrib
%{_mandir}/man1/codesnippets.*.gz

%{pkgdatadir}/AutoVersioning.zip
%{pkgdatadir}/BrowseTracker.zip
%{pkgdatadir}/Cccc.zip
%{pkgdatadir}/CppCheck.zip
%{pkgdatadir}/Cscope.zip
%{pkgdatadir}/DoxyBlocks.zip
%{pkgdatadir}/EditorConfig.zip
%{pkgdatadir}/EditorTweaks.zip
%{pkgdatadir}/FileManager.zip
%{pkgdatadir}/HexEditor.zip
%{pkgdatadir}/IncrementalSearch.zip
%{pkgdatadir}/MouseSap.zip
%{pkgdatadir}/ThreadSearch.zip
%{pkgdatadir}/ToolsPlus.zip
%{pkgdatadir}/Valgrind.zip
%{pkgdatadir}/byogames.zip
%{pkgdatadir}/cb_koders.zip
%{pkgdatadir}/clangd_client.zip
%{pkgdatadir}/codesnippets.zip
%{pkgdatadir}/codestat.zip
%{pkgdatadir}/copystrings.zip
%{pkgdatadir}/dragscroll.zip
%{pkgdatadir}/envvars.zip
%{pkgdatadir}/exporter.zip
%{pkgdatadir}/headerfixup.zip
%{pkgdatadir}/help_plugin.zip
%{pkgdatadir}/keybinder.zip
%{pkgdatadir}/lib_finder.zip
%{pkgdatadir}/Profiler.zip
%{pkgdatadir}/ProjectOptionsManipulator.zip
%{pkgdatadir}/RegExTestbed.zip
%{pkgdatadir}/ReopenEditor.zip
%{pkgdatadir}/SymTab.zip
%{pkgdatadir}/wxsmith.zip
%{pkgdatadir}/wxSmithAui.zip
%{pkgdatadir}/wxsmithcontribitems.zip
%{pkgdatadir}/images/wxsmith
%{pkgdatadir}/lib_finder
%{pkgdatadir}/NassiShneiderman.zip
%{pkgdatadir}/SpellChecker.zip
%{pkgdatadir}/SpellChecker
%{pkgdatadir}/SmartIndent*.zip
%{pkgdatadir}/rndgen.zip

%{plugindir}/libAutoVersioning.so
%{plugindir}/libBrowseTracker.so
%{plugindir}/libCccc.so
%{plugindir}/libCppCheck.so
%{plugindir}/libCscope.so
%{plugindir}/libDoxyBlocks.so
%{plugindir}/libEditorConfig.so
%{plugindir}/libEditorTweaks.so
%{plugindir}/libFileManager.so
%{plugindir}/libHexEditor.so
%{plugindir}/libIncrementalSearch.so
%{plugindir}/libMouseSap.so
%{plugindir}/libThreadSearch.so
%{plugindir}/libToolsPlus.so
%{plugindir}/libValgrind.so
%{plugindir}/libbyogames.so
%{plugindir}/libcb_koders.so
%{plugindir}/libclangd_client.so
%{plugindir}/libcodesnippets.so
%{plugindir}/libcodestat.so
%{plugindir}/libcopystrings.so
%{plugindir}/libdragscroll.so
%{plugindir}/libenvvars.so
%{plugindir}/libexporter.so
%{plugindir}/libheaderfixup.so
%{plugindir}/libhelp_plugin.so
%{plugindir}/libkeybinder.so
%{plugindir}/liblib_finder.so
%{plugindir}/libProfiler.so
%{plugindir}/libProjectOptionsManipulator.so
%{plugindir}/libRegExTestbed.so
%{plugindir}/libReopenEditor.so
%{plugindir}/libSymTab.so
%{plugindir}/libwxsmith.so
%{plugindir}/libwxSmithAui.so
%{plugindir}/libwxsmithcontribitems.so
%{plugindir}/libNassiShneiderman.so
%{plugindir}/libSpellChecker.so
%{plugindir}/libSmartIndent*.so
%{plugindir}/librndgen.so
%{_datadir}/metainfo/%{name}-contrib.metainfo.xml

%changelog
%autochangelog
