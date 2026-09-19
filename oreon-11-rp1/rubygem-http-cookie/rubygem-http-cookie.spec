%global source0_hash 75812d41b4e8d7437a6e36a206528a00ccb5ce5b3193d20be0c0e173abd21d91

%global	gem_name	http-cookie

Name:		rubygem-%{gem_name}
Version:	1.1.0
Release:	2%{?dist}

Summary:	Ruby library to handle HTTP Cookies based on RFC 6265
License:	MIT
URL:		https://github.com/sparklemotion/http-cookie
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
%dnl Source0:	https://github.com/sparklemotion/%{gem_name}/archive/v%{version}.tar.gz/#/%{gem_name}-%{version}.tar.gz
Source1:	%{gem_name}-%{version}-additional.tar.gz
# Source1 is created by $ bash %%SOURCE2 %%version
Source2:	%{gem_name}-create-missing-files.sh

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
# %%check
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(domain_name)
BuildRequires:	rubygem(sqlite3)
Requires:	ruby(rubygems)
Requires:	rubygem(domain_name)

BuildArch:	noarch

%description
HTTP::Cookie is a Ruby library to handle HTTP Cookies based on RFC 6265.  It
has with security, standards compliance and compatibility in mind, to behave
just the same as today's major web browsers.  It has builtin support for the
legacy cookies.txt and the latest cookies.sqlite formats of Mozilla Firefox,
and its modular API makes it easy to add support for a new backend store.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b 1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Clean up
rm -f %{buildroot}%{gem_cache}

%check
cp -a test/ .%{gem_instdir}
pushd .%{gem_instdir}
ruby -Ilib:test:. -e 'Dir.glob("test/test_*.rb").each {|f| require f}'
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/README.md

%{gem_libdir}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}/
%doc	%{gem_instdir}/CHANGELOG.md

%changelog
%autochangelog
