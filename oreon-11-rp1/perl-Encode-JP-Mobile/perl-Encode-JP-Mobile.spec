%global source0_hash db030eeba6ebf33bca496dd8c27abe148392eba6a68a2a1fe6244c036677dab3

Name:           perl-Encode-JP-Mobile
Version:        0.30
Release:        43%{?dist}
Summary:        Japan mobile phone Shift_JIS (CP932) / UTF-8 encoding
Summary(ja_JP): 日本の携帯電話向け Shift_JIS (CP932) / UTF-8 エンコーディング
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Encode-JP-Mobile-%{version}.tar.gz
# Fix a warning, CPAN RT#87393, bug #991873
Patch0:         Encode-JP-Mobile-0.30-Disable-a-test-for-kanji-name.patch
# Disable a failing test, CPAN RT#87393, bug #991873
Patch1:         Encode-JP-Mobile-0.30-Fix-warnings-counting-for-5.18.patch
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-Encode-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode) >= 2.23
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Encode::CJKConstants)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Encode::MIME::Name)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::ShareDir) >= 0.05
BuildRequires:  perl(MIME::Words) >= 5.428
BuildRequires:  perl(XSLoader)
# Tests:
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(YAML)
Requires:       perl(Encode) >= 2.23
Requires:       perl(File::ShareDir) >= 0.05
Requires:       perl(MIME::Words) >= 5.428

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Encode|File::ShareDir|MIME::Words)\\)$

%description
Encode::JP::Mobile extends Encode module with Japanese emoticons for mobile
phones mapped into private area of Unicode.

%description -l ja_JP
Encode::JP::Mobile は Encode 用の拡張モジュールで、日本の携帯電話用絵文字を
Unicode の私用領域 (PRIVATE AREA) にマッピングします。

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Encode-JP-Mobile-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR="$RPM_BUILD_ROOT"
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README TODO
%{perl_vendorarch}/*

%changelog
%autochangelog
