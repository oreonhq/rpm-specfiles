%global source0_hash 702fd1cdef9123e1871622a897727977c0933a420c50c94198f5bb22de8f0f8a

%global fontname ucs-miscfixed
%global fontconf 66-%{fontname}.conf

%global common_desc \
The usc-fixed-fonts package provides bitmap fonts for\
locations such as terminals.

Name: %{fontname}-fonts
Version: 0.3
Release: 37%{?dist}
License: LicenseRef-Fedora-Public-Domain
URL: http://www.cl.cam.ac.uk/~mgk25/ucs-fonts.html
Source0: https://www.cl.cam.ac.uk/~mgk25/download/ucs-fonts.tar.gz
Source1: 66-ucs-miscfixed.conf
BuildArch: noarch
Summary: Selected set of bitmap fonts
BuildRequires: fontpackages-devel
BuildRequires: mkfontdir bdftopcf fonttosfnt
Conflicts: ucs-miscfixed-opentype-fonts

%description
%common_desc

%package -n ucs-miscfixed-opentype-fonts
Summary:        Selected set of bitmap fonts (opentype version)
Conflicts:      ucs-miscfixed-fonts

%description -n ucs-miscfixed-opentype-fonts
%common_desc

This package contains the fonts in OpenType format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c
rm helvR12.bdf

%build
for i in `ls *.bdf`;
do fonttosfnt -v -b -c -g 2 -m 2 -o ${i%%.bdf}.otb $i;
done

%install
rm -rf $RPM_BUILD_ROOT

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.bdf %{buildroot}%{_fontdir}

install -m 0644 -p *.otb %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}


%_font_pkg -f %{fontconf} *.bdf

%doc README	

%_font_pkg -n ucs-miscfixed-opentype-fonts -f %{fontconf} *.otb

%doc README

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3-37
- Prepare for Oreon 11 (RP1)
