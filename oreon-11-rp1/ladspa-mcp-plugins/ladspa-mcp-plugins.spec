%global source0_hash 6c5bba81251ea03538ac3978279fea4065342b4267b0cd023dafca8268c84919

Name:           ladspa-mcp-plugins
Epoch:          1
Version:        0.4.0
Release:        37%{?dist}
Summary:        A set of audio plugins for LADSPA
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.kokkinizita.net/linuxaudio/
# Upstream site is down was
# http://www.kokkinizita.net/linuxaudio/downloads/...
Source:         MCP-plugins-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires: make
Requires:       ladspa
Obsoletes:      mcp-plugins <= 0.3.0-2
Provides:       mcp-plugins = %{version}-%{release}

%description
A set of audio plugins for LADSPA by Fons Adriaensen.
Currently contains a phaser, a chorus and a moog vcf.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n MCP-plugins-%{version}
sed -i -e "s|/usr/lib/ladspa|\\\$\(DESTDIR\)%{_libdir}/ladspa|g" \
    -e "s|-shared|-shared $RPM_LD_FLAGS|" Makefile
# we want to use the system ladspa.h
rm ladspa.h

%build
%make_build CPPFLAGS="$RPM_OPT_FLAGS -fPIC -D_REENTRANT"

%install
%{__mkdir} -p %{buildroot}%{_libdir}/ladspa
%make_install

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/ladspa/*.so

%changelog
%autochangelog
