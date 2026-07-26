%global source0_hash ef3de8319d691537b329053fae3a33195f8b070bbbfae8bf1a58c796081960e6

%global	gem_name	net-http-persistent

Summary:	Persistent connections using Net::HTTP plus a speed fix
Name:		rubygem-%{gem_name}
Version:	4.0.8
Release:	2%{?dist}
# SPDX confirmed
License:	MIT

URL:		https://github.com/drbrain/net-http-persistent
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(connection_pool)
BuildRequires:	rubygem(minitest)

Requires:	rubygems
BuildArch:	noarch

Provides:	rubygem(%{gem_name}) = %{version}

%description
Persistent connections using Net::HTTP plus a speed fix for 1.8.  It's
thread-safe too.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description    doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}/%{gem_dir}/

pushd %{buildroot}%{gem_instdir}
rm -rf \
	.autotest \
	.gemtest \
	.travis.yml \
	Gemfile \
	Manifest.txt \
	Rakefile \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}

# testrb -Ilib test
export RUBYLIB=$(pwd)/lib:$(pwd)
ruby -e 'Dir.glob("test/test_*.rb").each{|f| require f}'
popd

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/History.txt
%license	%{gem_instdir}/README.rdoc
%{gem_instdir}/lib/
%{gem_spec}
%exclude	%{gem_cache}

%files	doc
%{gem_docdir}/

%changelog
%autochangelog
