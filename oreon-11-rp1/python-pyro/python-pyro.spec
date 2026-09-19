%global source0_hash 511f5b0804e92dd77dc33adf9c947787e3f9e9c5a96b12162f0557a7c4ce21fb

%global pypi_name pyro

Name:           python-%{pypi_name}
Version:        4.82
Release:        %autorelease
Summary:        PYthon Remote Objects

License:        MIT
URL:            https://github.com/irmen/Pyro4/
Source0:        %{pypi_source Pyro4}
BuildArch:      noarch

%description
Pyro provides an object-oriented form of RPC. You can use Pyro within a
single system but also use it for IPC. For those that are familiar with
Java, Pyro resembles Java's Remote Method Invocation (RMI). It is less
similar to CORBA - which is a system- and language independent Distributed
Object Technology and has much more to offer than Pyro or RMI.

%package -n python3-%{pypi_name}
Summary:        Python Remote Objects

BuildRequires:  python3-devel

%description -n python3-%{pypi_name}
Pyro provides an object-oriented form of RPC. You can use Pyro within a
single system but also use it for IPC. For those that are familiar with
Java, Pyro resembles Java's Remote Method Invocation (RMI). It is less
similar to CORBA - which is a system- and language independent Distributed
Object Technology and has much more to offer than Pyro or RMI.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Pyro4-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
find examples -type f -exec sed -i 's/\r//' {} \;
find docs -type f -exec sed -i 's/\r//' {} \;
sed -i 's/\r//' LICENSE
chmod -x examples/echoserver/{Readme.txt,client.py}
chmod -x examples/gui_eventloop/{gui_threads.py,gui_nothreads.py}
chmod -x examples/maxsize/Readme.txt

%pyproject_install
%pyproject_save_files Pyro4
find examples -type f -exec sed -i 's/\r//' {} \;
find docs -type f -exec sed -i 's/\r//' {} \;
sed -i 's/\r//' LICENSE
chmod -x examples/echoserver/{Readme.txt,client.py}
chmod -x examples/gui_eventloop/{gui_threads.py,gui_nothreads.py}
chmod -x examples/maxsize/Readme.txt

%check
%pyproject_check_import -e Pyro4.utils.httpgateway

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc docs/* examples LICENSE
%{_bindir}/pyro4*

%changelog
%autochangelog
