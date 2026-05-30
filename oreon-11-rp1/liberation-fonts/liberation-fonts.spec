%global source0_hash 7191c669bf38899f73a2094ed00f7b800553364f90e2637010a69c0e268f25d0

%global archivename %{name}-ttf-%{version}
%define catalogue %{_sysconfdir}/X11/fontpath.d

BuildArch: noarch
BuildRequires:    mkfontscale mkfontdir

Epoch:      1
Version:    2.1.5
Release:    15%{?dist}
License:    OFL-1.1-RFN
URL:        https://github.com/liberationfonts/liberation-fonts

%global     fontlicenses    LICENSE
%global     fontdocs        AUTHORS ChangeLog README.md TODO
%global     fontdocsex      %{fontlicenses}

%global common_description %{expand:
The Liberation Fonts are intended to be replacements for the 3 most commonly\
used fonts on Microsoft systems: Times New Roman, Arial, and Courier New.}

%global fontpkgheaderall  %{expand:
Obsoletes: %{name} < %{epoch}:%{version}-%{release}
Provides:  %{name} = %{epoch}:%{version}-%{release}
}

%global fontfamily1       Liberation Sans
%global fontsummary1      Sans-serif fonts to replace commonly used Microsoft Arial
%global fontpkgheader1    %{expand:
Obsoletes: %{name}-common < %{epoch}:%{version}-%{release}
Provides:  %{name}-common = %{epoch}:%{version}-%{release}
}
%global fonts1            LiberationSans*.ttf
%global fontconfs1        %{SOURCE2}
%global fontdescription1  %{expand:
This package provides Sans-serif TrueType fonts that replace commonly used
Microsoft Arial.

%{common_description} }

%global fontfamily2       Liberation Serif
%global fontsummary2      Serif fonts to replace commonly used Microsoft Times New Roman
%global fontpkgheader2    %{expand:
Obsoletes: %{name}-common < %{epoch}:%{version}-%{release}
Provides:  %{name}-common = %{epoch}:%{version}-%{release}
}
%global fonts2            LiberationSerif*.ttf
%global fontconfs2        %{SOURCE3}
%global fontdescription2  %{expand:
This package provides Serif TrueType fonts that replace commonly used
Microsoft Times New Roman.

%{common_description} }

%global fontfamily3       Liberation Mono
%global fontsummary3      Monospace fonts to replace commonly used Microsoft Courier New
%global fontpkgheader3    %{expand:
Obsoletes: %{name}-common < %{epoch}:%{version}-%{release}
Provides:  %{name}-common = %{epoch}:%{version}-%{release}
}
%global fonts3            LiberationMono*.ttf
%global fontconfs3        %{SOURCE4}
%global fontdescription3  %{expand:
This package provides Monospace TrueType fonts that replace commonly used
Microsoft Courier New.

%{common_description} }

Source2:    59-liberation-mono-fonts.conf
Source3:    59-liberation-sans-fonts.conf
Source4:    59-liberation-serif-fonts.conf

Name:       liberation-fonts
Summary:    Fonts to replace commonly used Microsoft Windows fonts
Source0:        https://github.com/liberationfonts/liberation-fonts/files/7261482/liberation-fonts-ttf-2.1.5.tar.gz

%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{archivename}

%build
%fontbuild -a

%install
%fontinstall 
# fonts .ttf
# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

%fontinstall -z 1
mkfontscale %{buildroot}%{fontdir1}
mkfontdir %{buildroot}%{fontdir1}
ln -sf $(realpath --relative-to=%{buildroot}%{catalogue} %{buildroot}%{_fontbasedir})/%{fontpkgname1} %{buildroot}%{catalogue}/%{fontpkgname1}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/59-%{fontpkgname1}.conf
ln -sf $(realpath --relative-to=%{_fontconfig_confdir} %{_fontconfig_templatedir})/59-%{fontpkgname1}.conf %{buildroot}%{_fontconfig_confdir}/59-%{fontpkgname1}.conf

%fontinstall -z 2
mkfontscale %{buildroot}%{fontdir2}
mkfontdir %{buildroot}%{fontdir2}
ln -sf $(realpath --relative-to=%{buildroot}%{catalogue} %{buildroot}%{_fontbasedir})/%{fontpkgname2} %{buildroot}%{catalogue}/%{fontpkgname2}
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/59-%{fontpkgname2}.conf
ln -sf $(realpath --relative-to=%{_fontconfig_confdir} %{_fontconfig_templatedir})/59-%{fontpkgname2}.conf %{buildroot}%{_fontconfig_confdir}/59-%{fontpkgname2}.conf

%fontinstall -z 3
mkfontscale %{buildroot}%{fontdir3}
mkfontdir %{buildroot}%{fontdir3}
ln -sf $(realpath --relative-to=%{buildroot}%{catalogue} %{buildroot}%{_fontbasedir})/%{fontpkgname3} %{buildroot}%{catalogue}/%{fontpkgname3}
install -m 0644 -p %{SOURCE4} %{buildroot}%{_fontconfig_templatedir}/59-%{fontpkgname3}.conf
ln -sf $(realpath --relative-to=%{_fontconfig_confdir} %{_fontconfig_templatedir})/59-%{fontpkgname3}.conf %{buildroot}%{_fontconfig_confdir}/59-%{fontpkgname3}.conf


%check
%fontcheck -a

%fontfiles -z 1
%{catalogue}/%{fontpkgname1}
%verify(not md5 size mtime) %{fontdir1}/fonts.dir
%verify(not md5 size mtime) %{fontdir1}/fonts.scale
%ghost %attr(644, root, root) %{fontdir1}/.uuid

%fontfiles -z 2
%{catalogue}/%{fontpkgname2}
%verify(not md5 size mtime) %{fontdir2}/fonts.dir
%verify(not md5 size mtime) %{fontdir2}/fonts.scale
%ghost %attr(644, root, root) %{fontdir2}/.uuid

%fontfiles -z 3
%{catalogue}/%{fontpkgname3}
%verify(not md5 size mtime) %{fontdir3}/fonts.dir
%verify(not md5 size mtime) %{fontdir3}/fonts.scale
%ghost %attr(644, root, root) %{fontdir3}/.uuid



%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:2.1.5-15
- Import
