%global source0_hash 2951e4991214464c3e92107e46438527d23048e634f3aee91c719e0bdfaebda6
%global gem_name httpclient
%global rubyabi 1.8
%bcond_without tests
Summary:        HTTP Client interface for ruby
Name:           rubygem-%{gem_name}
Version:        2.8.3
Release:        1%{?dist}
License:        Ruby
URL:            https://github.com/nahi/httpclient
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:       ruby(release)
%if %{with tests}
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygem(http-cookie)
BuildRequires:  rubygem(mutex_m)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
an interface to HTTP Client for the ruby language

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version}

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/
find %{buildroot}/%{gem_instdir} -type f -name "*~" -delete
rm -rf %{buildroot}%{gem_instdir}/.yardoc
for file in `find %{buildroot}/%{gem_instdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done
for file in `find %{buildroot}/%{gem_instdir} -type f ! -perm /a+x -name "*.rb"`; do
    [ ! -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 755 $file
done
find %{buildroot}/%{gem_instdir} -type f -perm /g+wx -exec chmod -v g-w {} \;
find %{buildroot}/%{gem_instdir} -type f ! -perm /go+r -exec chmod -v go+r {} \;
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

pushd %{buildroot}%{gem_instdir}
rm -f test/test_auth.rb
ruby -Ilib -e 'Dir.glob "./test/test_*.rb", &method(:require)' -- \
  --ignore-name /^test_post_async_with_default_internal$/ \
  --ignore-name /^test_timeout$/ \
  --ignore-name /^test_tcp_keepalive$/ \
  --ignore-name /^test_sync$/ \
  --ignore-name /^test_proxy_ssl$/ \
  --ignore-name /^test_cert_store$/ \
  --ignore-name /^test_verification_without_httpclient$/ \
  --ignore-name /^test_verification$/ \
  --ignore-name /^test_set_default_paths$/ \
  --ignore-name /^test_allow_tlsv1$/ \
  --ignore-name /^test_no_sslv3$/ \
  --ignore-name /^test_post_connection_check$/ \
  --ignore-name /^test_debug_dev$/ \
  --ignore-name /^test_ciphers$/ \
  --ignore-name /^test_redirect_see_other$/ \
  --ignore-name /^test_post_follow_redirect$/ \
  --ignore-name /^test_put$/ \
  --ignore-name /^test_post_empty$/ \
  --ignore-name /^test_post_content$/ \
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-httpclient-doc -f %{oreon_filedir}/rubygem-httpclient-doc.list

%changelog

%autochangelog
