%global source0_hash db030eeba6ebf33bca496dd8c27abe148392eba6a68a2a1fe6244c036677dab3
Name:           perl-Encode-JP-Mobile
Version:        0.30
Release:        43%{?dist}
Summary:        Japan mobile phone Shift_JIS (CP932) / UTF-8 encoding
Summary(ja_JP): 日本の携帯電話向け Shift_JIS (CP932) / UTF-8 エンコーディング
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Encode-JP-Mobile-%{version}.tar.gz
Patch0:         Encode-JP-Mobile-0.30-Disable-a-test-for-kanji-name.patch
Patch1:         Encode-JP-Mobile-0.30-Fix-warnings-counting-for-5.18.patch
Requires:       perl(Encode) >= 2.23
Requires:       perl(File::ShareDir) >= 0.05
Requires:       perl(MIME::Words) >= 5.428
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Encode|File::ShareDir|MIME::Words)\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Alias)
BuildRequires:  perl(Encode::CJKConstants)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(Encode::MIME::Name)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(MIME::Words)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl-Encode-devel
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
