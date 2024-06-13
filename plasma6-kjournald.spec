#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Name: plasma6-kjournald
Version: 24.05.1
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/kjournald/-/archive/%{gitbranch}/kjournald-%{gitbranchd}.tar.bz2#/kjournald-%{git}.tar.bz2
%else
Source0:        https://invent.kde.org/system/%{name}/-/archive/master/%{name}-master.tar.bz2
%endif
%else
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/kjournald/-/archive/%{gitbranch}/kjournald-%{gitbranchd}.tar.bz2#/kjournald-%{git}.tar.bz2
%else
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/kjournald-%{version}.tar.xz
%endif
%endif
Summary: Graphical frontend for viewing the system journal
URL: https://github.com/kjournald/kjournald
License: GPL
Group: System
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlModels)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: pkgconfig(libsystemd)

%description
Graphical frontend for viewing the system journal

%prep
%autosetup -p1 -n kjournald-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang kjournald

%files -f kjournald.lang
%{_bindir}/kjournaldbrowser
%{_libdir}/libkjournald.so*
%{_datadir}/applications/org.kde.kjournaldbrowser.desktop
%{_datadir}/metainfo/org.kde.kjournaldbrowser.appdata.xml
%{_datadir}/qlogging-categories6/kjournald.categories
