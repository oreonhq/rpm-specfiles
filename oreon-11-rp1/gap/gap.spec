%global source0_hash none
%global gaparchdir %{_libdir}/gap
%global gaplibdir %{_datadir}/gap
%global icondir %{_datadir}/icons/hicolor
%global giturl  https://github.com/gap-system/gap
%global GAPDoc_files chooser.html lefttoc.css manual.css manual.js nocolorprompt.css ragged.css rainbow.js times.css toggless.css toggless.js
%bcond bootstrap 0
Name:           gap
Version:        4.15.1%{?prerel:~%{prerel}}
Release:        1%{?dist}
Summary:        Computational discrete algebra
%global majver  %{gsub %version ^(%d*%.%d*)%..*$ %1}
%global urlver  %{gsub %version ~ -}
License:        GPL-2.0-or-later
URL:            https://www.gap-system.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        gap-README.fedora
Source2:        update-gap-workspace
Source3:        gap.xml
Source4:        org.gap-system.gap.desktop
Source5:        org.gap-system.gap.metainfo.xml
Source6:        gap.1.in
Source7:        gac.1.in
Source8:        update-gap-workspace.1
Source9:        gap.vim
Source10:       gapicon.bmp
Patch:          %{name}-help.patch
Patch:          %{name}-popcount.patch
Patch:          %{name}-zlib-ng.patch
Patch:          %{name}-intptr-min.patch
Patch:          %{name}-signed-left-shift.patch
ExcludeArch:    %{ix86}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-online-help = %{version}-%{release}
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  gmp-devel
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  netpbm-progs
BuildRequires:  parallel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(readline)
BuildRequires:  pkgconfig(zlib-ng)
BuildRequires:  tex(color.sty)
BuildRequires:  tex(english.ldf)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(pslatex.sty)
BuildRequires:  tex(tex)
BuildRequires:  texlive-cm-super
BuildRequires:  texlive-ec
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-latex
BuildRequires:  texlive-psnfss
BuildRequires:  texlive-rsfs
BuildRequires:  texlive-symbol
BuildRequires:  texlive-times
BuildRequires:  vim-filesystem
# /oreon:deps
%description
GAP is a system for computational discrete algebra, with particular emphasis
on Computational Group Theory.  GAP provides a programming language, a library
of thousands of functions implementing algebraic algorithms written in the GAP
language as well as large data libraries of algebraic objects.  GAP is used in
research and teaching for studying groups and their representations, rings,
vector spaces, algebras, combinatorial structures, and more.

This package contains the command line application.

%package libs
Summary:        Essential GAP libraries
BuildArch:      noarch
%description libs
This package contains the essential GAP libraries: lib and grp.

%package core
Summary:        GAP core components
Requires:       %{name}-libs = %{version}-%{release}
%if %{without bootstrap}
Requires:       GAPDoc
Requires:       gap-pkg-primgrp
Requires:       gap-pkg-smallgrp
Requires:       gap-pkg-transgrp
%endif
Suggests:       catdoc
%description core
This package contains the core GAP system.

%package online-help
License:        GPL-2.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only AND LicenseRef-Rsfs
Summary:        Online help for GAP
Requires:       %{name}-core = %{version}-%{release}
BuildArch:      noarch
%description online-help
This package contains the documentation in TeX format needed for GAP's online
help system.

%package rpm-macros
Summary:        RPM macros for GAP packages
%description rpm-macros
This package contains RPM macros for GAP packages.

%package devel
Summary:        GAP compiler and development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-rpm-macros%{?_isa} = %{version}-%{release}
Requires:       gmp-devel%{?_isa}
%description devel
This package contains the GAP compiler (gac) and the header files necessary
for developing GAP programs.

%package vim
Summary:        Edit GAP files with VIM
Requires:       %{name}-core = %{version}-%{release}
Requires:       vim-filesystem
BuildArch:      noarch
%description vim
This package provides VIM add-on files to support editing GAP sources.  Both
syntax highlighting and indentation are supported.

# We used to have a separate libgap-devel package.  That has been removed
# because:
# - it only contained libgap.so;
# - sagemath, the only consumer of libgap, requires libgap.so in addition to
#   to the contents of the libgap package, so both had to be installed anyway

%package -n libgap
Summary:        Library containing core GAP logic
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       gzip
Recommends:     gap-pkg-autpgrp
Recommends:     gap-pkg-alnuth
Recommends:     gap-pkg-crisp
Recommends:     gap-pkg-ctbllib
Recommends:     gap-pkg-factint
Recommends:     gap-pkg-fga
Recommends:     gap-pkg-irredsol
Recommends:     gap-pkg-laguna
Recommends:     gap-pkg-packagemanager
Recommends:     gap-pkg-polenta
Recommends:     gap-pkg-polycyclic
Recommends:     gap-pkg-resclasses
Recommends:     gap-pkg-sophus
Recommends:     gap-pkg-tomlib
%description -n libgap
Library containing core GAP logic

%prep

%autosetup -p0 -n %{name}-%{urlver}

%conf
# Get the README
cp -p %{SOURCE1} README.fedora

# Regenerate the configure script
autoreconf -fi .

%build

export LDFLAGS='%{build_ldflags} -Wl,-z,lazy'
export STRIP=%{_bindir}/true
%configure --disable-maintainer-mode
%make_build V=1
%if %{without bootstrap}
make doc
%endif
cd doc
pdftex gapmacrodoc.tex
pdftex gapmacrodoc.tex
cd -
sed -i "s|$PWD|%{gapdir}|g" sysinfo.gap gac doc/make_doc
sed -i 's/[[:blank:]]*-pthread[[:blank:]]*//' sysinfo.gap
cat > macros.%{name} << EOF
%%gap_version %{version}
%%gap_archdir %{gaparchdir}
%%gap_libdir %{gaplibdir}
%%gapdoc_files %{GAPDoc_files}
%%gap_copy_docs(d:n:) \\
  subdir=%%{-d:%%{-d*}}%%{!-d:doc} \\
  if [ "%%_target_cpu" = "noarch" ]; then \\
    path=%%{buildroot}%%{gap_libdir}/pkg/%%{gap_upname}/\$subdir \\
  else \\
    path=%%{buildroot}%%{gap_archdir}/pkg/%%{gap_upname}/\$subdir \\
  fi \\
  for ext in bib css gif html jpeg jpg js lab pdf png six txt; do \\
    cp -p \$subdir/*.\$ext \$path 2>/dev/null || : \\
  done \\
  for fil in %%{gapdoc_files}; do \\
    if [ -e "\$path/\$fil" ]; then \\
      rm \$path/\$fil \\
      if [ "%%_target_cpu" = "noarch" ]; then \\
        ln -s ../..\$(sed 's|/|/..|' <<< "\${subdir//[^\\\\/]}")/GAPDoc/styles/\$fil \$path/\$fil \\
      else \\
        ln -s %%{gap_libdir}/pkg/GAPDoc/styles/\$fil \$path/\$fil \\
      fi \\
    fi \\
  done
EOF
%install
%make_install
chmod 0755 %{buildroot}%{_libdir}/libgap.so.*
rm %{buildroot}%{gaplibdir}/{*.md,COPYRIGHT,LICENSE}
rm -fr %{buildroot}%{gaplibdir}/etc/vim
install -p -m755 %{SOURCE2} %{buildroot}%{_bindir}
cp -p doc/{gapmacro.tex,manualindex,versiondata,*.{bib,lab,pdf,six,xml}} \
      %{buildroot}%{gaplibdir}/doc
mkdir -p %{buildroot}%{gaparchdir}/pkg
for book in hpc ref tut; do
    rm %{buildroot}%{gaplibdir}/doc/$book/{*.css,*.js,chooser.html}
    for fil in %{GAPDoc_files}; do
        ln -s ../../pkg/GAPDoc/styles/$fil %{buildroot}%{gaplibdir}/doc/$book
    done
done
mkdir -p %{buildroot}%{vimfiles_root}/indent
cp -p etc/vim/gap_indent.vim %{buildroot}%{vimfiles_root}/indent
mkdir -p %{buildroot}%{vimfiles_root}/syntax
cp -p etc/vim/gap.vim %{buildroot}%{vimfiles_root}/syntax
mkdir -p %{buildroot}%{vimfiles_root}/ftdetect
cp -p %{SOURCE9} %{buildroot}%{vimfiles_root}/ftdetect
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
touch %{buildroot}%{_localstatedir}/lib/%{name}/workspace.gz
bmptopnm %{SOURCE10} > gapicon.pnm
for size in 16 22 24 32 36 48 64 72 96 128 192 256 512; do
  mkdir -p %{buildroot}%{icondir}/${size}x${size}/apps
  pamscale -xsize=$size -ysize=$size gapicon.pnm | pnmtopng -compression=9 \
    > %{buildroot}%{icondir}/${size}x${size}/apps/%{name}.png
done
mkdir -p %{buildroot}%{_datadir}/mime/packages
cp -p %{SOURCE3} %{buildroot}%{_datadir}/mime/packages
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --mode=644 --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE4}
mkdir -p %{buildroot}%{_metainfodir}
install -pm 644 %{SOURCE5} %{buildroot}%{_metainfodir}
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gap-system.gap.metainfo.xml
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
cp -p macros.%{name} %{buildroot}%{_rpmconfigdir}/macros.d
mkdir -p %{buildroot}%{_mandir}/man1
sed 's|@VERSION@|%{version}|' %{SOURCE6} > %{buildroot}%{_mandir}/man1/gap.1
sed 's|@VERSION@|%{version}|' %{SOURCE7} > %{buildroot}%{_mandir}/man1/gac.1
cp -p %{SOURCE8} %{buildroot}%{_mandir}/man1
%oreon_autofiles libgap usr/*/lib*.so.*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.*

%preun

if [ $1 -eq 0 ]; then
  %{_bindir}/update-gap-workspace delete &> /dev/null || :
fi
%transfiletriggerin -- %{gaplibdir}/pkg %{gaparchdir}/pkg
%{_bindir}/update-gap-workspace > /dev/null || :
%transfiletriggerpostun -- %{gaplibdir}/pkg %{gaparchdir}/pkg
%{_bindir}/update-gap-workspace > /dev/null || :
%if %{without bootstrap}
%check

make check
%endif
%files -f %{oreon_filedir}/main.list
%files -n gap-libs -f %{oreon_filedir}/gap-libs.list
%files -n gap-core -f %{oreon_filedir}/gap-core.list
%files -n gap-online-help -f %{oreon_filedir}/gap-online-help.list
%files -n gap-rpm-macros -f %{oreon_filedir}/gap-rpm-macros.list
%files -n gap-devel -f %{oreon_filedir}/gap-devel.list
%files -n gap-vim -f %{oreon_filedir}/gap-vim.list
%files -n libgap -f %{oreon_filedir}/libgap.list

%changelog

%autochangelog
