%global source0_hash 494f8b05cf2e24db8de01b1a00234bd94ec2ecb384221307d91edfd498e9f08e
Name:           ikiwiki
Version:        3.20260201
Release:        1%{?dist}
Summary:        A wiki compiler
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://ikiwiki.info/
Source0:        https://ftp.debian.org/debian/pool/main/i/%{name}/%{name}_%{version}.orig.tar.xz
Patch0:         ikiwiki-libexecdir.patch
Patch1:         ikiwiki-fakehome.patch
Patch2:         ikiwiki-proxy_py.patch
BuildArch:      noarch
Requires:       perl(CGI::FormBuilder) >= 3.02.02
Requires:       perl(CGI::Session)
Requires:       perl(Digest::SHA)
Requires:       perl(HTML::Scrubber)
Requires:       perl(Image::Magick)
Requires:       perl(Mail::Sendmail)
Requires:       perl(Sys::Syslog)
Requires:       perl(Text::Markdown)
Requires:       perl(XML::Simple)
Requires:       perl(YAML::XS)
%if "%{?python3_version}" != ""
Requires:       python(abi) = %{python3_version}
%endif
Requires:       python%{python3_pkgversion}-docutils
Provides:       perl(IkiWiki::Render)
Provides:       perl(IkiWiki::UserInfo)
%global cgi_bin %{_libexecdir}/w3m/cgi-bin
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(IkiWiki\\)$
%global __provides_exclude %{?__provides_exclude:%{__provides_exclude}|}^perl\\(IkiWiki\\)$
# oreon:deps
BuildRequires:  bzr
BuildRequires:  coreutils
BuildRequires:  cvs
BuildRequires:  cvsps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  mercurial
BuildRequires:  perl(B)
BuildRequires:  perl(CGI::FormBuilder)
BuildRequires:  perl(CGI::Session)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::MimeInfo)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ReadBackwards)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::chdir)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::LinkExtor)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::Scrubber)
BuildRequires:  perl(HTML::Tagset)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open2)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(Locale::Po4a::Chooser)
BuildRequires:  perl(Locale::Po4a::Po)
BuildRequires:  perl(Mail::Sendmail)
BuildRequires:  perl(Memoize)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(RPC::XML)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Markdown)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::SAX)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(XML::Twig)
BuildRequires:  perl(YAML::XS)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(open)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  sed
BuildRequires:  subversion
# /oreon:deps
%description
Ikiwiki is a wiki compiler. It converts wiki pages into HTML pages
suitable for publishing on a website. Ikiwiki stores pages and history
in a revision control system such as Subversion or Git. There are many
other features, including support for blogging, as well as a large
array of plugins.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ikiwiki-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

# goes into the -w3m subpackage
cat << \EOF > README.fedora
See http://ikiwiki.info/w3mmode/ for more information.
EOF

# Drop Monotone plugin
# Monotone depends on botan v1, which has been EOL for a long time
rm -v IkiWiki/Plugin/monotone.pm

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
make
%check

make test || :
%install
make pure_install DESTDIR=%{buildroot} W3M_CGI_BIN=%{cgi_bin}
%find_lang %{name}
mkdir -p %{buildroot}%{_libexecdir}/ikiwiki/plugins
mv %{buildroot}%{_prefix}/lib/ikiwiki/plugins/* \
   %{buildroot}%{_libexecdir}/ikiwiki/plugins
sed -e '1{/^#!/d}' -i \
    %{buildroot}%{_sysconfdir}/ikiwiki/auto.setup \
    %{buildroot}%{_sysconfdir}/ikiwiki/auto-blog.setup \
    %{buildroot}%{_libexecdir}/ikiwiki/plugins/proxy.py \
    %{buildroot}%{_libexecdir}/ikiwiki/plugins/rst
sed -e '1i#!%{__python3}' -i \
    %{buildroot}%{_libexecdir}/ikiwiki/plugins/rst
find %{buildroot}%{perl_vendorlib}/IkiWiki -type f \
     -exec chmod -x {} \;
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%package w3m
Summary:        Ikiwiki w3m cgi meta-wrapper
Requires:       w3m
Requires:       %{name} = %{version}-%{release}
%description w3m
Enable usage of all of ikiwiki's web features (page editing, etc) in
the w3m web browser without a web server. w3m supports local CGI
scripts, and ikiwiki can be set up to run that way using the
meta-wrapper in this package.

%files -f %{oreon_filedir}/main.list
%files -n ikiwiki-w3m -f %{oreon_filedir}/ikiwiki-w3m.list

%changelog

%autochangelog
