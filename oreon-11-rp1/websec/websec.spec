%global source0_hash 13899c8d9fda00f6ee9be2917abd362d3cc1037af136e9f389ce92f7ebb63f3a

Name:           websec
Version:        1.9.0
Release:        41%{?dist}
Summary:        Web Secretary - Web page monitoring software with highlighting

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/baruch/websec
Source0:        websec-1.9.0.tar.gz
# Patch0: newer GNU Make versions (3.82, maybe older as well) get confused by
# parts of the Makefile that are unused anyway, so remove them with this patch;
# upstream is dead afaics
Patch0:         %{name}-disable-htmldocs
# Patch1: Background in https://bugzilla.redhat.com/show_bug.cgi?id=1254288
# not send upstream, as its dead
Patch1:         %{name}-silence-unescaped-left-brace-warnings.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  /usr/bin/pod2man
BuildRequires:  perl-generators

# needed to send mail:
Requires:       /usr/sbin/sendmail
# needed for ssl:
Requires:       perl(IO::Socket::SSL)
Requires:       perl(LWP::Protocol::https)

%description
Web Secretary is a web page change monitoring software. It will detect changes
based on content analysis, making sure that it's not just HTML that changed,
but actual content. You can tell it what to ignore in the page (hit counters
and such), and it can mail you the document with the changes highlighted or 
load the highlighted page in a browser.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .patch0
%patch -P1 -p1 -b .patch1

%build
make PREFIX=%{_prefix} %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT .__doc
make install DESTDIR=$RPM_BUILD_ROOT PREFIX=%{_prefix}

# proper permissions for man pages
chmod 0644 $RPM_BUILD_ROOT%{_datadir}/man/man*/*

# temp doc dir 
mv $RPM_BUILD_ROOT%{_datadir}/doc/websec .__doc

# having the next two in the proper place would require proper dependencies,
# which is probably not worth the trouble as that would be bloat for most 
# users; so ship them as doc, that's better then not shipping them at all
mv $RPM_BUILD_ROOT%{_datadir}/vim/vim61 $RPM_BUILD_ROOT%{_datadir}/emacs/ \
   .__doc/
mkdir .__doc/scripts
cp rollback htmldiff .__doc/scripts/
chmod -x .__doc/scripts/*

%files
%doc COPYING HACKING NEWS TODO .__doc/*
%{_bindir}/*
%{_datadir}/man/man*/*

%changelog
%autochangelog
