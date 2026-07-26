%global source0_hash d0f95dc98f57bb2e940817b10a92660d9e378d48668295761c0b12a46c6f96dc

Name:           techtalk-pse
Version:        1.2.0
Release:        20%{?dist}
Summary:        Presentation software designed for technical people

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://git.annexia.org/?p=techtalk-pse.git;a=summary
# No website hosts the tarballs at present:
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Glib)
BuildRequires:  perl(Gtk3)
BuildRequires:  perl(Gtk3::WebKit)
BuildRequires:  perl(Glib::Object::Introspection)
BuildRequires:  vte291
BuildRequires:  /usr/bin/pod2man

# This shouldn't have to be explicit but it is omitted from the
Requires: vte291

%description
Tech Talk PSE is is Linux Presentation Software designed by technical people to
give technical software demonstrations to other technical people. It is
designed to be simple to use (for people who know how to use an editor and the
command line) and powerful, so that you can create informative, technically
accurate and entertaining talks and demonstrations.

Tech Talk PSE is good at opening editors at the right place, opening shell
prompts with preloaded history, compiling and running things during the
demonstration, displaying text, photos, figures and video.

Tech Talk PSE is bad at slide effects, chart junk and bullet points.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
echo '// empty' >> examples/simple/code.js

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%doc COPYING README TODO examples
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
