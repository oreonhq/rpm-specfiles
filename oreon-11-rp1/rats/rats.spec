%global source0_hash 2163ad111070542d941c23b98d3da231f13cf065f50f2e4ca40673996570776a

Name:           rats
Version:        2.4
Release:        31%{?dist}
Summary:        Rough Auditing Tool for Security
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://code.google.com/p/rough-auditing-tool-for-security/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/rough-auditing-tool-for-security/rats-%{version}.tgz
Patch1:         0002-Fix-engine-output-and-php-extension.patch
Patch2:         0003-Fix-report-layout.patch
Patch3:         rats-2.4-gtk-vuln.patch
Patch5:		rats-configure-c99.patch
BuildRequires: make
BuildRequires:  expat-devel
BuildRequires:  flex
BuildRequires:  gcc

%description
RATS(Rough Auditing Tool for Security) scans through code, finding potentially
dangerous function calls. The goal of this tool is not to definitively find 
bugs (yet). The current goal is to provide a reasonable starting point for 
performing manual security audits.

The initial vulnerability database is taken directly from things that could be 
easily found when starting with the forthcoming book, "Building Secure 
Software" by Viega and McGraw.  

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# $(DESTDIR) hack.
sed -e 's/$(BINDIR)/$(DESTDIR)$(BINDIR)/g' \
    -e 's/ $(LIBDIR)/ $(DESTDIR)$(LIBDIR)/g' \
    -e 's/$(MANDIR)/$(DESTDIR)$(MANDIR)/g' \
    -e 's/ $(SHAREDIR)/ $(DESTDIR)$(SHAREDIR)/g' -i Makefile.in

%build
%configure --datadir=%{_datadir}/%{name}
%make_build lex && %make_build

%install
%make_install

%files
%doc COPYING README
%{_bindir}/rats
%{_datadir}/rats
%{_mandir}/man1/rats.1*

%changelog
%autochangelog
