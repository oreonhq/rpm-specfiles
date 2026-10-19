%global source0_hash 3467ce2f70a9a3fbbf8d4d97355a2f334a6351baa6722251403637a8cbebf6b7
%global srcver 20040629
%global catalogue %{_sysconfdir}/X11/fontpath.d
Name: sazanami-fonts
Version: 0.%{srcver}
Release:        50%{?dist}
URL:     http://efont.sourceforge.jp/
%global foundry           Sazanami
%global fontlicense       BSD-3-Clause
%global fontlicenses      LICENSE.shinonome LICENSE_J.mplus
%global fontdocs          README.sazanami README.kappa README.ayu doc/misaki/misakib8.txt README.oradano
%global fontdocsex        %{fontlicenses}
%global common_description %{expand:The Sazanami type faces are automatically generated from Wadalab font kit.
They also contains some embedded Japanese bitmap fonts.
}
%global fontfamily0       Sazanami Gothic
%global fontsummary0      Sazanami Gothic Japanese TrueType font
%global fontpkgheader0    %{expand:
Obsoletes: sazanami-fonts-common < %{version}-%{release}
Provides: sazanami-fonts-common = %{version}-%{release}
}
%global fonts0            sazanami-gothic.ttf
%global fontsex0          %{nil}
%global fontconfs0        %{SOURCE10}
%global fontconfsex0      %{nil}
%global fontdescription0  %{expand:
%{common_description}
This package contains Japanese TrueType font for Gothic type face.
}
%global fontfamily1       Sazanami Mincho
%global fontsummary1      Sazanami Mincho Japanese TrueType font
%global fontpkgheader1    %{expand:
Obsoletes: sazanami-fonts-common < %{version}-%{release}
Provides: sazanami-fonts-common = %{version}-%{release}
}
%global fonts1            sazanami-mincho.ttf
%global fontsex1          %{nil}
%global fontconfs1        %{SOURCE11}
%global fontconfsex1      %{nil}
%global fontdescription1  %{expand:
%{common_description}
This package contains Japanese TrueType font for Mincho type face.
}
Source0:        http://globalbase.dl.sourceforge.jp/efont/10087/sazanami-%{srcver}.tar.bz2
Source1:  fonts.alias.sazanami-gothic
Source2:  fonts.alias.sazanami-mincho
Source10: 70-%{fontpkgname0}.conf
Source11: 70-%{fontpkgname1}.conf
Patch0:   uni7E6B-gothic.patch
Patch1:   uni7E6B-mincho.patch
Patch2:   uni8449-mincho.patch
Summary:        Sazanami Japanese TrueType fonts
License: BSD-3-Clause
BuildArch: noarch
# oreon:deps
BuildRequires:  fonts-rpm-macros
BuildRequires:  fonttools
BuildRequires:  mkfontdir
BuildRequires:  ttmkfdir
BuildRequires:  xorg-x11-fonts-misc
# /oreon:deps
%description
%{common_description}

# “fontpkg” will generate the font subpackage headers corresponding to the
# elements declared above.
# “fontpkg” accepts the following selection arguments:
# – “-a”          process everything
# – “-z [number]” process a specific declaration block
# If no flag is specified it will only process the zero/nosuffix block.
%fontpkg -z 0 -s

%fontpkg -z 1

# “fontmetapkg” will generate a font meta(sub)package header for all the font
# subpackages generated in this spec. Optional arguments:
# – “-n [name]”      use [name] as metapackage name
# – “-s [variable]”  use the content of [variable] as metapackage summary
# – “-d [variable]”  use the content of [variable] as metapackage description
# – “-z [numbers]”   restrict metapackaging to [numbers] comma-separated list
#                    of font package suffixes
%fontmetapkg

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n sazanami-%{srcver}

%build

%fontbuild -a
ttx -i -a -e sazanami-gothic.ttf
patch -b -z .uni7E6B sazanami-gothic.ttx %{PATCH0}
touch -r sazanami-gothic.ttf sazanami-gothic.ttx
rm sazanami-gothic.ttf
ttx -b sazanami-gothic.ttx
touch -r sazanami-gothic.ttx sazanami-gothic.ttf
ttx -i -a -e sazanami-mincho.ttf
patch -b -z .uni7E6B sazanami-mincho.ttx %{PATCH1}
patch -b -z .uni8449 sazanami-mincho.ttx %{PATCH2}
touch -r sazanami-mincho.ttf sazanami-mincho.ttx
rm sazanami-mincho.ttf
ttx -b sazanami-mincho.ttx
touch -r sazanami-mincho.ttx sazanami-mincho.ttf
mv doc/shinonome/LICENSE LICENSE.shinonome
mv doc/mplus/LICENSE_J LICENSE_J.mplus
mv README README.sazanami
mv doc/kappa/README README.kappa
mv doc/ayu/README.txt README.ayu
mv doc/oradano/README.txt README.oradano
%install
install -dm 0755 $RPM_BUILD_ROOT%{catalogue}
%fontinstall -z 0
install -pm 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname0}/fonts.alias
ttmkfdir -d $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname0} -o $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname0}/fonts.scale
mkfontdir $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname0}
ln -sf $(realpath --relative-to=$RPM_BUILD_ROOT%{catalogue} $RPM_BUILD_ROOT%{_fontbasedir})/%{fontpkgname0} $RPM_BUILD_ROOT%{catalogue}/%{fontpkgname0}
%fontinstall -z 1
install -pm 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname1}/fonts.alias
ttmkfdir -d $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname1} -o $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname1}/fonts.scale
mkfontdir $RPM_BUILD_ROOT%{_fontbasedir}/%{fontpkgname1}
ln -sf $(realpath --relative-to=$RPM_BUILD_ROOT%{catalogue} $RPM_BUILD_ROOT%{_fontbasedir})/%{fontpkgname1} $RPM_BUILD_ROOT%{catalogue}/%{fontpkgname1}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%fontcheck -a
%fontfiles -z 0
%{catalogue}/%{fontpkgname0}
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname0}/fonts.dir
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname0}/fonts.scale
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname0}/fonts.alias
%fontfiles -z 1
%{catalogue}/%{fontpkgname1}
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname1}/fonts.dir
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname1}/fonts.scale
%verify(not md5 size mtime) %{_fontbasedir}/%{fontpkgname1}/fonts.alias
%files -f %{oreon_filedir}/main.list
%files -n adf-gillius-fonts -f %{oreon_filedir}/adf-gillius-fonts.list
%files -n google-go-fonts -f %{oreon_filedir}/google-go-fonts.list
%files -n sazanami-fonts-all -f %{oreon_filedir}/sazanami-fonts-all.list

%changelog

%autochangelog
