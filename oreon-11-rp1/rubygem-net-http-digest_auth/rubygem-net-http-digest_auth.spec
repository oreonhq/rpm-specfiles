%global source0_hash 4b8ad50ed8d180a58db5d6c49449b987dd0466fe01e24037945bc007562a08db

%global	gem_name	net-http-digest_auth
%if		0%{?fedora} < 19
%global	rubyabi	1.9.1
%endif

Summary:	Implementation of RFC 2617 - Digest Access Authentication
Name:		rubygem-%{gem_name}
Version:	1.4.1
Release:	19%{?dist}

# README.txt
License:	MIT
URL:		http://docs.seattlerb.org/net-http-digest_auth
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

%if 0%{?fedora} >= 19
Requires:	ruby(release)
BuildRequires:	ruby(release)
%else
Requires:	ruby(abi) = %{rubyabi}
Requires:	ruby
BuildRequires:	ruby(abi) = %{rubyabi}
BuildRequires:	ruby
%endif

Requires:	ruby(rubygems) 
BuildRequires:	rubygems-devel 
# %%check
BuildRequires:	rubygem(minitest)
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
An implementation of RFC 2617 - Digest Access Authentication.  At this time
the gem does not drop in to Net::HTTP and can be used for with other HTTP
clients.
In order to use net-http-digest_auth you'll need to perform some request
wrangling on your own.  See the class documentation at Net::HTTP::DigestAuth
for an example.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T

TOPDIR=$(pwd)
mkdir tmpunpackdir
pushd tmpunpackdir

gem unpack %{SOURCE0}
cd %{gem_name}-%{version}

# For minitest 4.7.0 (latest is 5.0.x)
sed -i -e 's|MiniTest::Test|MiniTest::Unit::TestCase|' \
	test/test_net_http_digest_auth.rb

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
mkdir -p .%{gem_dir}
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Clean up
pushd %{buildroot}%{gem_instdir}
rm -f  \
	.autotest \
	.gemtest \
	.travis.yml \
	%{nil}
popd

%check
pushd .%{gem_instdir}
ruby -Ilib test/test_net_http_digest_auth.rb
popd

%files
%dir	%{gem_instdir}/
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile

%{gem_libdir}/
%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}/
%doc	%{gem_instdir}/sample/
%exclude	%{gem_instdir}/test/

%changelog
%autochangelog
