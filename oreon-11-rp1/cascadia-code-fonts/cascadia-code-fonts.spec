%global source20_hash e67a68ee3386db63f48b9054bd196ea752bc6a4ebb4df35adce6733da50c8474
%global source0_hash 4ea145a56f35a61d8b5523b949df166b21e5db57313ba4223c490accbf816822
%global fontname cascadia
%global fontconf 60-%{fontname}-code-fonts.conf
%global fontconfmono 57-%{fontname}-mono-fonts.conf
%global fontconfmononf 60-%{fontname}-mono-nf-fonts.conf
%global fontconfmonopl 60-%{fontname}-mono-pl-fonts.conf
%global fontconfnf 60-%{fontname}-code-nf-fonts.conf
%global fontconfpl 60-%{fontname}-code-pl-fonts.conf
%bcond fromsource 0
Name:		%{fontname}-code-fonts
Summary:        A mono-spaced font designed for programming and terminal emulation
Version:	2407.24
Release:        4%{?dist}
License:	OFL-1.1-RFN
URL:		https://github.com/microsoft/cascadia-code/
Source0:        https://github.com/microsoft/cascadia-code/archive/v%{version}.tar.gz
Source1:	%{fontconf}
Source2:	%{fontname}-code.metainfo.xml
Source3:	%{fontconfmono}
Source4:	%{fontname}-mono.metainfo.xml
Source5:	%{fontconfmonopl}
Source6:	%{fontname}-mono-pl.metainfo.xml
Source7:	%{fontconfpl}
Source8:	%{fontname}-code-pl.metainfo.xml
Source9:	%{fontconfnf}
Source10:	%{fontname}-code-nf.metainfo.xml
Source11:	%{fontconfmononf}
Source12:	%{fontname}-mono-nf.metainfo.xml
%if %{with fromsource}
%else
Source20:	https://github.com/microsoft/cascadia-code/releases/download/v%{version}/CascadiaCode-%{version}.zip
%endif
BuildArch:	noarch
Requires:	fontpackages-filesystem
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cascadia-code-fonts = %{version}-%{release}
# /oreon:deps
%description
Cascadia Code is a mono-spaced font designed to provide a fresh experience for
command line experiences and code editors. Notably, it supports programming
ligatures.

%package -n %{fontname}-mono-fonts
Summary:	A mono-spaced font family designed for terminal emulation
%description -n %{fontname}-mono-fonts
The Cascadia Mono font family is a variant of Cascadia Code, without
programming ligatures.

%package -n %{fontname}-mono-nf-fonts
Summary:	A mono-spaced font family with the "nerd fonts" symbols
%description -n %{fontname}-mono-nf-fonts
The Cascadia Mono NF font family is a variant of Cascadia Code, without
programming ligatures, and with the "nerd fonts" symbols.

%package -n %{fontname}-mono-pl-fonts
Summary:	A mono-spaced font family with power line symbols
%description -n %{fontname}-mono-pl-fonts
The Cascadia Mono PL font family is a variant of Cascadia Code, without
programming ligatures, and with power line symbols.

%package -n %{fontname}-code-nf-fonts
Summary:	A mono-spaced font family with ligatures and the "nerd fonts" symbols
%description -n %{fontname}-code-nf-fonts
The Cascadia Code NF font family is a variant of Cascadia Code, with the
"nerd fonts" symbols.

%package -n %{fontname}-code-pl-fonts
Summary:	A mono-spaced font family with ligatures and power line symbols
%description -n %{fontname}-code-pl-fonts
The Cascadia Code PL font family is a variant of Cascadia Code, with power line
symbols.

%package -n %{fontname}-fonts-all
Summary:	A meta-package to enable easy installation of all Cascadia font families
Requires:	%{fontname}-code-fonts
Requires:	%{fontname}-code-nf-fonts
Requires:	%{fontname}-code-pl-fonts
Requires:	%{fontname}-mono-fonts
Requires:	%{fontname}-mono-nf-fonts
Requires:	%{fontname}-mono-pl-fonts
%description -n %{fontname}-fonts-all
This is a meta-package which enables easy installation of all Cascadia font
families.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{fontname}-code-%{version}

# correct end-of-line encoding
for i in OFL-FAQ.txt FONTLOG.txt README.md; do
	sed -i 's/\r//' $i
done

%if %{with fromsource}
%build

%if %{with fromsource}
%{python3} build.py
%else
unzip %{SOURCE20}
%endif
%install
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-code-fonts/
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-code-nf-fonts/
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-code-pl-fonts/
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-mono-fonts/
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-mono-nf-fonts/
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{fontname}-mono-pl-fonts/
install -m 0644 -p otf/static/CascadiaCode-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-code-fonts/
install -m 0644 -p otf/static/CascadiaCodeNF-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-code-nf-fonts/
install -m 0644 -p otf/static/CascadiaCodePL-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-code-pl-fonts/
install -m 0644 -p otf/static/CascadiaMono-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-mono-fonts/
install -m 0644 -p otf/static/CascadiaMonoNF-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-mono-nf-fonts/
install -m 0644 -p otf/static/CascadiaMonoPL-*.otf %{buildroot}%{_fontbasedir}/%{fontname}-mono-pl-fonts/
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/
install -m 0644 -p %{SOURCE3} %{buildroot}%{_fontconfig_templatedir}/
install -m 0644 -p %{SOURCE5} %{buildroot}%{_fontconfig_templatedir}/
install -m 0644 -p %{SOURCE7} %{buildroot}%{_fontconfig_templatedir}/
install -m 0644 -p %{SOURCE9} %{buildroot}%{_fontconfig_templatedir}/
install -m 0644 -p %{SOURCE11} %{buildroot}%{_fontconfig_templatedir}/
ln -s %{_fontconfig_templatedir}/%{fontconf} %{buildroot}%{_fontconfig_confdir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconfmono} %{buildroot}%{_fontconfig_confdir}/%{fontconfmono}
ln -s %{_fontconfig_templatedir}/%{fontconfmonopl} %{buildroot}%{_fontconfig_confdir}/%{fontconfmonopl}
ln -s %{_fontconfig_templatedir}/%{fontconfpl} %{buildroot}%{_fontconfig_confdir}/%{fontconfpl}
ln -s %{_fontconfig_templatedir}/%{fontconfnf} %{buildroot}%{_fontconfig_confdir}/%{fontconfnf}
ln -s %{_fontconfig_templatedir}/%{fontconfmononf} %{buildroot}%{_fontconfig_confdir}/%{fontconfmononf}
install -Dm 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/appdata/%{fontname}-code.metainfo.xml
install -Dm 0644 -p %{SOURCE4} %{buildroot}%{_datadir}/appdata/%{fontname}-mono.metainfo.xml
install -Dm 0644 -p %{SOURCE6} %{buildroot}%{_datadir}/appdata/%{fontname}-mono-pl.metainfo.xml
install -Dm 0644 -p %{SOURCE8} %{buildroot}%{_datadir}/appdata/%{fontname}-code-pl.metainfo.xml
install -Dm 0644 -p %{SOURCE10} %{buildroot}%{_datadir}/appdata/%{fontname}-code-nf.metainfo.xml
install -Dm 0644 -p %{SOURCE12} %{buildroot}%{_datadir}/appdata/%{fontname}-mono-nf.metainfo.xml
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files

%changelog

%autochangelog
%endif
