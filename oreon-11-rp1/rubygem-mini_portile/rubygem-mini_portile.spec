%global source0_hash 5c60cd85db3df6b279e9a6807954c596dc0ced359a10fcd9b49969a6aa8d7d40

%global	gem_name	mini_portile

Name:		rubygem-%{gem_name}
Version:	0.6.2
Release:	22%{?dist}
Summary:	Simplistic port-like solution for developers
License:	MIT

URL:		http://github.com/flavorjones/mini_portile
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch

Provides: rubygem(%{gem_name}) = %{version}-%{release}

%description
Simplistic port-like solution for developers. It provides a standard and
simplified way to compile against dependency libraries without messing up
your system.

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

# Permission
find . -name \*.rb -print0 | xargs --null chmod 0644

gem specification -l --ruby %{SOURCE0} > %{gem_name}.gemspec
gem build %{gem_name}.gemspec
mv %{gem_name}-%{version}.gem $TOPDIR

popd
rm -rf tmpunpackdir

%build
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%files
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*
%exclude	%{gem_instdir}/Rakefile
%{gem_libdir}/

%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}/
# Currently no useful
%exclude	%{gem_instdir}/examples/

%changelog
%autochangelog
