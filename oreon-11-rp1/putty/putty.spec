%global source0_hash 718777c13d63d0dff91fe03162bc2a05b4dfc8b0827634cd60b51cefdff631c6

Name:		putty
Version:	0.83
Release:	4%{?dist}
Summary:	SSH, Telnet and Rlogin client
License:	MIT
URL:		http://www.chiark.greenend.org.uk/~sgtatham/putty/
Source0:	http://the.earth.li/~sgtatham/putty/latest/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.svg
Source3:	uk.org.greenend.chiark.sgtatham.putty.metainfo.xml
BuildRequires:	gtk3-devel
BuildRequires:	krb5-devel
BuildRequires:	halibut
BuildRequires:	desktop-file-utils
BuildRequires:	ImageMagick
BuildRequires:	perl-Digest-SHA
BuildRequires:	coreutils
BuildRequires:	python3-devel
BuildRequires:	sed
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	cmake
Requires:	hicolor-icon-theme
# https://bugzilla.redhat.com/show_bug.cgi?id=2442271
Requires:	gdk-pixbuf2-modules-extra

%description
Putty is a SSH, Telnet & Rlogin client - this time for Linux.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# fix python shebangs to use python3 (python bits aren't currently packaged)
find . -type f -name "*.py" -exec sed -i '/^#!/ s|.*|#!%{__python3}|' {} \;

%build
export CFLAGS="%{build_cflags} -DNOT_X_WINDOWS -Wno-error=unused-function"
%cmake
%cmake_build
make -C icons putty-48.png
%cmake_build -t doc

%install
%cmake_install
install -d html
install -pm 0644 doc/html/*.html html

desktop-file-install \
  --vendor "" \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

install -m644 -D -p icons/putty-48.png %{buildroot}%{_datadir}/pixmaps/putty.png
install -m644 -D -p %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/putty.svg

install -m644 -D -p %{SOURCE3} %{buildroot}%{_metainfodir}/uk.org.greenend.chiark.sgtatham.putty.metainfo.xml

%files
%doc LICENCE html
%{_bindir}/*
%{_mandir}/man1/*.1*
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/uk.org.greenend.chiark.sgtatham.putty.metainfo.xml

%changelog
%autochangelog
