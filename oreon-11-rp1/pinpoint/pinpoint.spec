%global source0_hash 5a207dd1a35681b7268e6aa5ff9b2c5381f4cc63e5f2e5695997ca9d3264e8ca

Name:           pinpoint
Version:        0.1.8
Release:        24%{?dist}
Summary:        A tool for making hackers do excellent presentations

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://wiki.gnome.org/Apps/Pinpoint
Source0:        https://download.gnome.org/sources/pinpoint/0.1/pinpoint-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  clutter-devel >= 1.4
BuildRequires:  clutter-gst3-devel
BuildRequires:  clutter-gtk-devel
BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  glib2-devel
BuildRequires:  librsvg2-devel

%description
Pinpoint a simple presentation tool that hopes to avoid audience death
by bullet point and instead encourage presentations containing
beautiful images and small amounts of concise text in slides.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%license COPYING
%doc AUTHORS NEWS README introduction.pin *.jpg
%{_bindir}/pinpoint
%{_datadir}/pinpoint

%changelog
%autochangelog
