%global source0_hash 95e234cde474cd62ee762f45f8c9d8297436c61ac53bc6af7a73c257358c4bd0

Name:           perl-Clipboard
Version:        0.32
Release:        3%{?dist}
Summary:        Copy and paste with any OS
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Clipboard
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Clipboard-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.28
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(File::Spec)
# Tests
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  xclip
BuildRequires:  xsel
Requires:       perl(CGI)
Requires:       perl(IPC::Open2)
Requires:       perl(URI::Escape)
Requires:       xclip
%if 0%{?fedora} || 0%{?rhel} >= 9
Recommends:     wl-clipboard
%endif

%description
Who doesn't remember the first time they learned to copy and paste, and
generated an exponentially growing text document? Yes, that's right,
clipboards are magical.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Clipboard-%{version}

# no need for Win32 or MacPasteboard
rm lib/Clipboard/MacPasteboard.pm
rm lib/Clipboard/Win32.pm

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes README.mkdn
%{perl_vendorlib}/Clipboard*
%{_bindir}/clip*
%{_mandir}/man1/clip*1*
%{_mandir}/man3/Clipboard*

%changelog
%autochangelog
