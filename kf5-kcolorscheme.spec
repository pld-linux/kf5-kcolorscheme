#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.249.0
%define		qtver		5.15.2
%define		kfname		kcolorscheme

Summary:	Color Scheme
Name:		kf5-%{kfname}
Version:	5.249.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	2d412530ee3e9e51b02e95d32e610072
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-tools
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6DBus >= %{qtver}
Requires:	Qt6Widgets >= %{qtver}
Requires:	kf5-dirs
Requires:	kf5-kauth >= %{version}
Requires:	kf5-kcodecs >= %{version}
Requires:	kf5-kconfig >= %{version}
Requires:	kf5-kcoreaddons >= %{version}
Requires:	kf5-kguiaddons >= %{version}
Requires:	kf5-ki18n >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
Classes to read and interact with KColorScheme.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cmake >= 3.16
Requires:	kf5-kauth-devel >= %{version}
Requires:	kf5-kcodecs-devel >= %{version}
Requires:	kf5-kconfig-devel >= %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}6

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libKF6ColorScheme.so.*.*.*
%ghost %{_libdir}/libKF6ColorScheme.so.6
%{_datadir}/qlogging-categories6/kcolorscheme.categories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KColorScheme
%{_libdir}/cmake/KF6ColorScheme
%{_libdir}/libKF6ColorScheme.so
