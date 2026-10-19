%global source0_hash ef3de8319d691537b329053fae3a33195f8b070bbbfae8bf1a58c796081960e6
%global	gem_name	net-http-persistent
Summary:        Persistent connections using Net::HTTP plus a speed fix
Name:		rubygem-%{gem_name}
Version:	4.0.8
Release:        1%{?dist}
License:	MIT
URL:		https://github.com/drbrain/net-http-persistent
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires:	ruby(release)
Requires:	rubygems
BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(connection_pool)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
export RUBYLIB=$(pwd)/lib:$(pwd)
ruby -e 'Dir.glob("test/test_*.rb").each{|f| require f}'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-net-http-persistent-doc -f %{oreon_filedir}/rubygem-net-http-persistent-doc.list

%changelog

%autochangelog
