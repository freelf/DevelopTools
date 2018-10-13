//
//  <#ClassName#>Reducer.swift
//
//  Created by Beyond on 2018/6/6.
//  Copyright © 2018年 张东坡. All rights reserved.
//

import Foundation

struct <#ClassName#>State: StateType {
    //存储 view 的状态
}
enum <#ClassName#>Action: ActionType {
    //这里相当于一个动作

}
enum <#ClassName#>Command: CommandType {
    //这里是一个动作引发的一些 command，比如一个 load 操作，需要 view 显示一个 loadingView，可以通过 command 来进行网络操作，而 Action 设置 state 的 loading 状态。还有一些跳转的操作也通过 command 来进行操作
}
class <#ClassName#>Reducer {
    //它就是一个函数，y = f(x)在这里就是 (newState,command?) = Reducer(Action,oldState),通过对 Action 解析来返回新状态，然后会调用 owner 的 stateDidChange
    lazy var reducer: ((<#ClassName#>State,<#ClassName#>Action) -> (state: <#ClassName#>State, command: <#ClassName#>Command?)) = { [weak self] (state: <#ClassName#>State, action: <#ClassName#>Action) in
        var state = state
        var command: <#ClassName#>Command? = nil
        switch action {
            //这里解析 Action，然后生成新的 State和必要的 command。
        }
        return (state,command)
    }
    weak var owner: <#ClassName#>ViewController?
    init(owner: <#ClassName#>ViewController) {
        self.owner = owner
    }
}
